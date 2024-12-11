#Cargamos el data llamado "datos1.csv"
library(data.table)
library(dplyr) 
library(ggplot2)
library(gtsummary)
library(skimr)
library(stringr)


datos<- fread("C:/Users/Marisol/AV1/No country/Cuidado/datos1.csv")

# Mostrar la estructura del DataFrame 
str(datos)

# Mostrar las primeras filas del DataFrame 
head(datos)

# Contar los valores de la columna 'status' 
table(datos$status)
# Cargar librería dplyr
library(dplyr)

# Calcular los porcentajes de los valores en la columna 'status'
porcentaje_status <- datos %>%
  count(status) %>%
  mutate(percentage = n / sum(n) * 100)
print(porcentaje_status)


# GRAFICOS!
# Gráfico de barras para la columna 'status' 
status_counts <- table(datos$status) 
barplot(status_counts, main = "Distribución de URLs Legítimas y de Phishing", 
        col = c("green", "red"), names.arg = c("Phishing", "Legítimo"), 
        ylab = "Cantidad", xlab = "Status")





# Gráfico de dispersión con ggplot2
ggplot(datos, aes(x = log10(largo_host + 1), y = log10(url_length + 1), color = factor(status, labels = c("Phishing", "Legítimo")))) +
  geom_point() +
  labs(title = "Log(Largo del Host) vs. Log(Longitud de la URL)", x = "Log(Largo del Host)", y = "Log(Longitud de la URL)") +
  scale_color_manual(values = c("green", "red")) +
  theme_minimal()




#Grafico de la sumatoria de status vs caracteres especiales 
# Sumar los valores de las columnas de caracteres especiales para cada fila
# Lista de las columnas de caracteres especiales
special_char_columns <- c("count_!", "count_@", "count_#", "count_$", "count_%", 
                          "count_^", "count_&", "count_*", "count_(", "count_)", 
                          "count__", "count_+", "count_-", "count_=", "count_[", 
                          "count_]", "count_{", "count_}", "count_|", "count_,", 
                          "count_:", "count_'", "count_,", "count_.", "count_<", 
                          "count_>", "count_?", "count_/", "count_\\" )

# Sumar los valores de las columnas de caracteres especiales para cada fila
datos <- datos %>%
  mutate(total_special_chars = rowSums(select(., all_of(special_char_columns))))

# Calcular el promedio total de caracteres especiales por status 
promedio_special_chars_by_status <- datos %>% 
  group_by(status) %>% 
  summarise(promedio_special_chars = mean(total_special_chars, na.rm = TRUE)) 
print(promedio_special_chars_by_status)

# Ajustar los márgenes del gráfico
par(mar = c(5, 4, 4, 2) + 0.1)

# Crear un gráfico de barras para el promedio total de caracteres especiales por status 
barplot(
  promedio_special_chars_by_status$promedio_special_chars, 
  main = "Distribución de Caracteres Especiales por Status", 
  col = c("red", "green"), 
  names.arg = c("Phishing", "Legítimo"), 
  ylab = "Promedio de Caracteres Especiales", 
  xlab = "Status" 
)

#Grafico de distribucion los caracteres repetidos en las ulrs, phishing y legitimos
# Boxplot de caracteres repetidos por status
boxplot(repeated_chars ~ factor(status, labels = c("Phishing", "Legítimo")), data = datos, 
        col = c("red", "green"), main = "Distribución de Caracteres Repetidos por Status", 
        xlab = "Status", ylab = "Caracteres Repetidos")






#Grafico de promedio de letras en las urls phishing y legitimos

# Función para contar letras en una URL
contar_letras <- function(url) {
  sum(str_count(url, "[a-zA-Z]"))
}

# Aplicar la función a cada URL y añadir los resultados al DataFrame
datos <- datos %>%
  mutate(total_letters = sapply(url, contar_letras))

# Calcular el promedio total de letras por status
promedio_letters_by_status <- datos %>%
  group_by(status) %>%
  summarise(promedio_letters = mean(total_letters, na.rm = TRUE))

print(promedio_letters_by_status)

# Ajustar los márgenes del gráfico
par(mar = c(5, 4, 4, 2) + 0.1)

# Crear un gráfico de barras para el promedio total de letras por status
barplot(
  promedio_letters_by_status$promedio_letters,
  main = "Promedio de Letras por Status",
  col = c("red", "green"),
  names.arg = c("Phishing", "Legítimo"),
  ylab = "Promedio de Letras",
  xlab = "Status"
)



# Gráfico de barras para la proporción de subdominios por estado
ggplot(datos, aes(x = factor(num_subdomains), fill = factor(status, levels = c(-1, 1), labels = c("Phishing", "Legítimo")))) +
  geom_bar(position = "dodge") +
  labs(title = "Proporción de Subdominios por Status", x = "Número de Subdominios", y = "Cantidad", fill = "Status") +
  scale_fill_manual(values = c("red", "green")) +
  theme_minimal()


# Gráfico de barras para la distribución de prefijos fuera de lugar
barplot(table(datos$prefijos_fuera_de_lugar), col = "purple", main = "Distribución de Prefijos Fuera de Lugar", 
        xlab = "Prefijos Fuera de Lugar", ylab = "Cantidad")












#Resumen Estadistico

summary(datos)


# Visualización de una matriz de correlación
cor_matrix <- cor(datos %>% select_if(is.numeric), use = "complete.obs")
#la columna space_count tiene una varianza de cero, el calcude correlacion no procede para esa columna


#Filtramos los URLs en dos grupos, phishing y legitimate
# Filtrar las URLs de phishing
datos_phishing <- datos %>%
  filter(status == -1)

# Filtrar las URLs legítimas
datos_legitimos <- datos %>%
  filter(status == 1)

# Verificar los resultados
print("Datos de Phishing:")
print(head(datos_phishing))

print("Datos Legítimos:")
print(head(datos_legitimos))



# Calcular los promedios de las columnas (excepto 'url') en datos de phishing
resumen <- datos_phishing %>%
  select(-status) %>%
  summarise(across(where(is.numeric), mean, na.rm = TRUE))
print(resumen)


# Calcular los promedios de las columnas (excepto 'url') en datos legítimos
resumen <- datos_legitimos %>%
  select(-status) %>%
  summarise(across(where(is.numeric), mean, na.rm = TRUE))
print(resumen)












