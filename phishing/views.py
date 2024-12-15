import os
import pickle
import pandas as pd
import re
import string
from django.shortcuts import render, redirect
from .forms import ExternalDataForm
import joblib
import numpy as np
from .models import LibraryC
from django.http import HttpResponse


model2 = joblib.load('ensayo_/modelo21(-1)_redes_neuronales_19_033.pkl')
feature_names_in_ = ['has_https', 'has_http', 'has_ftp', 'has_www', 'has_ip', 'url_length', 'largo_host', 'longitud_palabra_mas_corta', 'ratio_digitos_url', 'ratio_digitos_host', 'repeated_chars', 'space_count', 'num_subdomains', 'prefijos_fuera_de_lugar', 'count_a_lower', 'count_b_lower', 'count_c_lower', 'count_d_lower', 'count_e_lower', 'count_f_lower', 'count_g_lower', 'count_h_lower', 'count_i_lower', 'count_j_lower', 'count_k_lower', 'count_l_lower', 'count_m_lower', 'count_n_lower', 'count_o_lower', 'count_p_lower', 'count_q_lower', 'count_r_lower', 'count_s_lower', 'count_t_lower', 'count_u_lower', 'count_v_lower', 'count_w_lower', 'count_x_lower', 'count_y_lower', 'count_z_lower', 'count_A_upper',
                     'count_B_upper', 'count_C_upper', 'count_D_upper', 'count_E_upper', 'count_F_upper', 'count_G_upper', 'count_H_upper', 'count_I_upper', 'count_J_upper', 'count_K_upper', 'count_L_upper', 'count_M_upper', 'count_N_upper', 'count_O_upper', 'count_P_upper', 'count_Q_upper', 'count_R_upper', 'count_S_upper', 'count_T_upper', 'count_U_upper', 'count_V_upper', 'count_W_upper', 'count_X_upper', 'count_Y_upper', 'count_Z_upper', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'count_!', 'count_@', 'count_#', 'count_$', 'count_%', 'count_^', 'count_&', 'count_*', 'count_(', 'count__', 'count_+', 'count_-', 'count_[', 'count_{', 'count_|', 'count_;', 'count_:', "count_'", 'count_,', 'count_<', 'count_?', 'count_/']



def home_view(request):
    #photo= LibraryC.objects.all()
    #cloudy_img={'photo':photo}
    return render(request,'home.html')


def phishing_view(request):
    photo= LibraryC.objects.all()
    cloudy_img={'photo':photo}
    return render(request,'phishingurl24.html',{'photo':photo})

#data = os.path.join('ensayo_','datos6_solo_url_status.csv')
def features_view(url):
    datas = pd.DataFrame({'url': [url]})
    #datas= pd.read_csv(data)
    #datas = datas.drop ('status', axis = 1)
    valores_nulos_data1 = datas.isnull().sum()
   # print('null', valores_nulos_data1)
    espacios_vacios_data1 = datas.apply(
        lambda x: isinstance(x, str) and x.strip() == '').sum()
   # print('vacios', espacios_vacios_data1)
    valores = datas['url'].unique()
    #print('unicos', valores)
    for df in [datas]:
        duplicados = df.duplicated().sum()
        df.drop_duplicates(inplace=True)
        eliminado = duplicados
    #print('duplic', eliminado)
    prefixes = ['https://', 'http://', 'ftp://', 'ftps://', 'mailto://', 'file://',
                'data://', 'tel://', 'ldap://', 'news://', 'nntp://', 'telnet://', 'gopher://']

    def count_prefixes(url):
        # Inicializa el conteo de cada prefijo
        counts = {prefix: 0 for prefix in prefixes}
        for prefix in prefixes:
            if url.startswith(prefix):
                # Incrementa el conteo si el prefijo coincide
                counts[prefix] += 1
        return counts
    # prefix_counts = datas['url'].apply(count_prefixes)
    # datas['prefix_counts'] = datas['prefix'].value_counts()
    www_count = datas['url'].str.startswith('www.').sum()
    ip_count = datas['url'].str.match(r'^\d{1,3}(\.\d{1,3}){3}').sum()
    urls_malformadas = datas['url'].str.startswith(('httpss://', 'htps://'))

    def has_prefix(url, prefix):
        return 1 if url.startswith(prefix) else 0

    def starts_with_ip(url):
        ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}')
        return 1 if ip_pattern.match(url) else 0
    datas['has_https'] = datas['url'].apply(
        lambda x: has_prefix(x, 'https://'))
    datas['has_http'] = datas['url'].apply(lambda x: has_prefix(x, 'http://'))
    datas['has_ftp'] = datas['url'].apply(lambda x: has_prefix(x, 'ftp://'))
    datas['has_www'] = datas['url'].apply(lambda x: has_prefix(x, 'www.'))
    datas['has_ip'] = datas['url'].apply(starts_with_ip)

    def host_length(url):
        parts = url.split('/')
        if len(parts) > 2:
            return len(parts[2])
        else:
            return -1

    def longest_word_length(url):
        words = url.split('/')
        return max((len(word) for word in words), default=-1)

    def shortest_word_length(url):
        words = url.split('/')
        return min((len(word) for word in words if word), default=-1)

    def average_word_length(url):
        words = url.split('/')
        return sum(len(word) for word in words) / len(words) if words else -1

    def digit_ratio(url):
        if len(url) == 0:
            return -1
        digits = sum(c.isdigit() for c in url)
        return digits / len(url)

    def host_digit_ratio(url):
        parts = url.split('/')
        if len(parts) > 2:
            host = parts[2]
            digits = sum(c.isdigit() for c in host)
            return digits / len(host) if len(host) > 0 else 0
        else:
            return -1
    # Añadir nuevas columnas antes de estandarizar las URLs
    datas['url_length'] = datas['url'].apply(len)
    datas['largo_host'] = datas['url'].apply(host_length)
    # datas['longitud_palabra_mas_larga'] = datas['url'].apply(longest_word_length)
    datas['longitud_palabra_mas_corta'] = datas['url'].apply(
        shortest_word_length)
    # datas['promedio_palabra_por_fila'] = datas['url'].apply(average_word_length)
    datas['ratio_digitos_url'] = datas['url'].apply(digit_ratio)
    datas['ratio_digitos_host'] = datas['url'].apply(host_digit_ratio)
    duplicados = datas.duplicated().sum()
    datas.drop_duplicates(inplace=True)
    alfabeto_minuscula = string.ascii_lowercase
    alfabeto_mayuscula = string.ascii_uppercase
    caracteres_str = "!@#$%^&*(_+-[{|;:',<?/"
    caracteres = list(caracteres_str)
    numeros = "0123456789"
    # Definir los prefijos de interés
    pref_interes = ['https', 'http', 'ftp', 'ftps', 'mailto', 'file', 'data', 'tel',
                    'ldap', 'news', 'nntp', 'telnet', 'gopher', 'www', 'm', 'api', 'rss', 'atom']

    def caracteres_repet(url):
        count = 0
        for i in range(1, len(url)):
            if url[i] == url[i-1]:
                count += 1
        return count

    def count_spaces(url):
        return url.count(' ')

    def count_chars(url, chars):
        return {char: url.count(char) for char in chars}

    def count_subdomains(url):
        url = re.sub(r'^(http://|https://|ftp://|www\.)', '', url)
        return url.count('.')
    # Función para identificar prefijos fuera de lugar

    def find_misplaced_prefix(url):
        # Verificar si el prefijo aparece fuera del inicio de la URL
        for prefijo in pref_interes:
            pattern = fr'^{prefijo}\.|.+{re.escape(prefijo)}.*'
            if re.search(pattern, url) and not url.startswith(f"{prefijo}."):
                return 1  # prefijo fuera de lugar
        return 0  # todos los prefijos estan en su lugar correcto
    # Calcular nuevas características
    df_new = pd.DataFrame({
        'repeated_chars': datas['url'].apply(caracteres_repet),
        'space_count': datas['url'].apply(count_spaces),
        # 'num_special_chars': datas['url'].apply(lambda x: sum(x.count(c) for c in caracteres)),
        'num_subdomains': datas['url'].apply(lambda x: x.count('.')),
        'prefijos_fuera_de_lugar': datas['url'].apply(find_misplaced_prefix)
    })
    # Añadir columnas para cada letra minúscula
    for char in alfabeto_minuscula:
        df_new[f'count_{char}_lower'] = datas['url'].apply(
            lambda x: x.count(char))
    # Añadir columnas para cada letra MAYUSCULA
    for char in alfabeto_mayuscula:
        df_new[f'count_{char}_upper'] = datas['url'].apply(
            lambda x: x.count(char))
    # Añadir columnas para cada número
    for num in numeros:
        df_new[num] = datas['url'].apply(lambda x: x.count(num))
    # Añadir columnas para cada carácter especial
    for char in caracteres:
        col_name = f"count_{char}"
        df_new[col_name] = datas['url'].apply(lambda x: x.count(char))
    # Unir las nuevas columnas al DataFrame original
    datas = pd.concat([datas, df_new], axis=1)
    # Mover la columna 'status' al final de las columnas
    if 'status' not in datas.columns:
        datas['status'] = 0
        columns = [col for col in datas.columns if col !=
                   'status'] + ['status']
        #print('estas son las columnas del dataset', datas.columns)
    # datas = datas[columns]
    # columns = [col for col in datas.columns if col != 'status'] + ['status']
    # datas = datas[columns]
    # Verificar y encontrar duplicados en el DataFrame
    duplicados = datas[datas.duplicated(subset=['url'], keep=False)]
    # Contar y mostrar duplicados
    total_duplicados = duplicados.shape[0]
    # Eliminar duplicados manteniendo solo la primera ocurrencia
    datas_sin_duplicados = datas.drop_duplicates(subset=['url'])
    datas = datas_sin_duplicados
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}')
    filtered = datas[datas['url'].str.match(ip_pattern)]
    # Contar el número total de duplicados
    duplicados = filtered[filtered.duplicated(subset='url', keep=False)]
    conteo_duplicados = duplicados['url'].value_counts()
    total_duplicados = conteo_duplicados.sum()
    # print(f"Total de URLs duplicadas: {total_duplicados}")
    # eliminado duplicados del data
    datas_actualizado = datas.drop_duplicates(subset='url', keep='first')
    # print("Se ha eliminado URLs duplicadas por IP")
    # actualizar el data original sin las urls duplicadas
    datas_actualizado = datas[~datas.index.isin(duplicados.index)]
    # verificamos q se han eliminado
    ip_pattern2 = re.compile(r'^(\d{1,3}\.){3}\d{1,3}')
    filtered2 = datas_actualizado[datas_actualizado['url'].str.match(
        ip_pattern)]
    conteo_duplicados2 = filtered2.duplicated(subset='url', keep=False).sum()
    output_file = os.path.join('analisisRN(-1)_url21.csv')
    datas_actualizado.to_csv(output_file, index=False)

    return output_file


def external_data_view(request):
    if request.method == 'POST':
        form = ExternalDataForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url_externa']
            print('URL ingresada:', url)    
            # Llamar a features_view para analizar la URL y guardar en CSV
            csv_file_path = features_view(url)
            # print('Ruta del archivo CSV generado:', csv_file_path)    
            try:
                df_analysis = pd.read_csv(csv_file_path)
            except FileNotFoundError:
                return render(request, 'error.html', {'message': 'Archivo CSV no encontrado.'})
            except Exception as e:
                return render(request, 'error.html', {'message': f'Error al leer el CSV: {e}'}) 
            # expected_columns = feature_names_in_  
            try:
                features = df_analysis.drop(
                    columns=['url', 'status'], errors='ignore')
                # features = ajustes_features(features, expected_columns)
            except Exception as e:
                return render(request, 'error.html', {'message': f'Error al procesar las características: {e}'})    
            try:
                predictions = model2.predict(features)
            except Exception as e:
                return render(request, 'error.html', {'message': f'Error al realizar la predicción: {e}'})
            # print(features.head())
            # print(features.columns)
            df_analysis['predictions'] = predictions
            
            resultado=df_analysis['predictions'][0]
            print("prediccion",resultado)
            predictions_output_file = os.path.join(
                'ensayo_', 'predictionsRN_21(-1).csv')
            df_analysis.to_csv(predictions_output_file, index=False)  
            photo=LibraryC.objects.all()  
            # return redirect('mostrarcsv')
            # return mostrar_csv_view(predictions_output_file)
            cloudy_img={'photo':photo}
            return render(request, 'prediccion.html', {'url': url, 'prediction': resultado,'photo':photo})   
        else:
            form = ExternalDataForm()
    return render(request, 'phishingurl24.html',{'photo':photo})

