import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.status_code)
    categories = response.json()
    for category in categories:
        print(category['name'])
    # return response.json()


    ['autor', 'avance', 'counting', 'estatus', 'extInm', 'extInm1', 'extInm2', 'extPos', 'extPos1', 'extPos2', 'free', 'id', 'n_1_1', 'n_1_1Sug', 'n_1_1Tx', 'n_1_2', 'n_1_2Sug', 'n_1_2Tx', 'n_1_3', 'n_1_3Sug', 'n_1_3Tx', 'n_2_1', 'n_2_1Sug', 'n_2_1Tx', 'n_2_2', 'n_2_2Sug', 'n_2_2Tx', 'n_2_3', 'n_2_3Sug', 'n_2_3Tx', 'n_3_1', 'n_3_1Sug', 'n_3_1Tx', 'n_3_2', 'n_3_2Sug', 'n_3_2Tx', 'n_3_3', 'n_3_3Sug', 'n_3_3Tx', 'n_3a3Inf', 'n_4_1', 'n_4_1Sug', 'n_4_1Tx', 'n_4_2', 'n_4_2Sug', 'n_4_2Tx', 'n_4_3', 'n_4_3Sug', 'n_4_3Tx', 'n_4a4', 'n_6a6Inf', 'n_6a6Inf2', 'n_6a6Sup', 'n_NA', 'n_alturaFInfR1', 'n_alturaFInfR2', 'n_alturaFInfR3', 'n_alturaFInfR4', 'n_alturaFInfR5', 'n_alturaFIntR1', 'n_alturaFIntR2', 'n_alturaFIntR5', 'n_alturaFacialInf', 'n_alturaInferior', 'n_alturaInferiorMm', 'n_apinamientoInf', 'n_apinamientoSup', 'n_bimler', 'n_biotipo', 'n_cajaDental', 'n_consultorio', 'n_denticion', 'n_diferencia4_4', 'n_diferencia4_4KorkhauseMod', 'n_diferencia6_6', 'n_diferencia6_6KorkhauseMod', 'n_diferenciaLongAnt', 'n_diferenciaLongAntKorkhauseMod', 'n_discrepancia', 'n_discrepanciaSug', 'n_discrepanciaSugerencia', 'n_distancia4_4', 'n_distancia4_4KorkhauseMod', 'n_distancia6_6', 'n_distancia6_6KorkhauseMod', 'n_distanciaLongAnt', 'n_distanciaLongAntKorkhauseMod', 'n_dxIIoIII', 'n_edad', 'n_ejeFacial', 'n_ejeIncisivoInf', 'n_ejeIncisivoInfDx', 'n_ejeIncisivoSup', 'n_ejeIncisivoSupDx', 'n_fecha', 'n_formaArcadaInf', 'n_formaArcadaSup', 'n_girosApinamientoInf', 'n_girosKorkhause', 'n_girosKorkhauseMod', 'n_girosMordidaCruzada', 'n_loAnt', 'n_locdePorion', 'n_longMandR1', 'n_longMandR2', 'n_longMandR3', 'n_longMandR4', 'n_longitudMandibular', 'n_longitudMaxilar', 'n_mm', 'n_mordidaAnterior', 'n_mordidaAnteriorMm', 'n_mordidaPosteriorDer', 'n_mordidaPosteriorIzq', 'n_nombre', 'n_observacionPanoramica', 'n_obsevacionesOclusion', 'n_odonto_d12', 'n_odonto_d13', 'n_odonto_d14', 'n_odonto_d15', 'n_odonto_d16', 'n_odonto_d17', 'n_odonto_d18', 'n_odonto_d21', 'n_odonto_d22', 'n_odonto_d24', 'n_odonto_d25', 'n_odonto_d26', 'n_odonto_d27', 'n_odonto_d28', 'n_odonto_d31', 'n_odonto_d32', 'n_odonto_d33', 'n_odonto_d34', 'n_odonto_d35', 'n_odonto_d36', 'n_odonto_d37', 'n_odonto_d38', 'n_odonto_d41', 'n_odonto_d42', 'n_odonto_d44', 'n_odonto_d45', 'n_odonto_d46', 'n_odonto_d47', 'n_odonto_d48', 'n_odonto_r11', 'n_odonto_r12', 'n_odonto_r13', 'n_odonto_r14', 'n_odonto_r15', 'n_odonto_r16', 'n_odonto_r17', 'n_odonto_r18', 'n_odonto_r21', 'n_odonto_r22', 'n_odonto_r23', 'n_odonto_r24', 'n_odonto_r25', 'n_odonto_r26', 'n_odonto_r27', 'n_odonto_r28', 'n_odonto_r31', 'n_odonto_r32', 'n_odonto_r33', 'n_odonto_r34', 'n_odonto_r35', 'n_odonto_r36', 'n_odonto_r37', 'n_odonto_r38', 'n_odonto_r41', 'n_odonto_r42', 'n_odonto_r43', 'n_odonto_r44', 'n_odonto_r45', 'n_odonto_r46', 'n_odonto_r47', 'n_odonto_r48', 'n_planoDeOclusion', 'n_planoMandibular', 'n_relacionCaninaDer', 'n_relacionCaninaIzq', 'n_relacionEsqueletica', 'n_relacionEsqueleticaMm', 'n_relacionMolarDer', 'n_relacionMolarIzq', 'n_segMolarInf', 'n_segMolarInfDx', 'n_sum1_1Inf', 'n_sum1_1InfSug', 'n_sum1_1Sup', 'n_sum1_1Sup75', 'n_sum1_1Sup75Red', 'n_sum1_1Sup75RedSug', 'n_sum1_1Sup75Sug', 'n_sum1_1SupKorkhause', 'n_sum1_1SupKorkhauseMod', 'n_sum1_1SupSug', 'n_tamanoArcadaInf', 'n_tamanoArcadaSup', 'n_tendenciaVertical', 'n_tipoExpansionSeleccionado', 'n_witts', 'obsDoctor', 'planDoctor', 'rehDoctor', 'selec_apin', 'selec_kork', 'selec_korkM', 'selec_morC', 'tdSug_11', 'tdSug_12', 'tdSug_13', 'tdSug_21', 'tdSug_22', 'tdSug_23', 'tdSug_31', 'tdSug_32', 'tdSug_33', 'tdSug_41', 'tdSug_42', 'tdSug_43', 'tdtx_11', 'tdtx_12', 'tdtx_13', 'tdtx_21', 'tdtx_22', 'tdtx_23', 'tdtx_31', 'tdtx_32', 'tdtx_33', 'tdtx_41', 'tdtx_42', 'tdtx_43', 'u_fechaTrazado', 'urlTrazado', 'z']