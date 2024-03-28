def verificar_ancora(valor):
    if valor in ['PASCHOAL_2203']:
        return 'DROGARIA PASCHOAL PIRES LTDA'
    
    elif valor in ['KOYAMA_2203']:
        return 'KOYAMA FARMACIA E PERFUMARIA EIRELI'
    
    elif valor in ['PAPBRAUN_2203']:
        return 'PAPELARIA BRAUN NUNES LTDA'

    elif valor in ['EMDASILVA_2203']:
        return 'E. M. DA SILVA NUNES'    

    elif valor in ['SWAROWSKY_2203']:
        return 'SWAROWSKI E KROTH'    
    
    elif valor in ['JSPERSCH_2203']:
        return 'J S PERSCH COMÉRCIO DE ALIMENTOS'    

    elif valor in ['CARNESINGLATERRA_2203',
                    'CARNESPRATES_2203',
                    'CARNESPHOENIX_2203',
                    'CARNESEGM_2203',
                    'CARNESSAMPAIO_2203',
                    'CARNESPANTANAL_2203',
                   
                    ]:
        return 'CASA DE CARNES INGLATERRA'    

    elif valor in ['BAIKA_2203']:
        return 'BAIKA PIZZARIA PASSO FUNDO'    

    elif valor in ['SUPERGUERREIRO_2203']:
        return 'S GUERREIRO SUPERMERCADOS'    

    elif valor in ['JOAQUIM_2203', 
                   'JOAQUIM1_2203']:
        return 'JOAQUIM CRISPIM E CIA LTDA'    

    elif valor in ['ccc4fd8d-f8e7-49e6-9b8f-d925cf102d13_581227-0_581227-2']:
        return 'CARUS COMERCIO DE ALIMENTOS LTDA'    

    elif valor in ['BOZETTI_2203']:
        return 'BOZETTI E BATEZINI'    
    
    elif valor in ['RSFOLTZ_2203', 'RSFOLTZ1_2203']:
        return 'RS FOLTZ'    
    
    elif valor in ['SUPERBUINO_2203',
                    'SUPERERBUINO2_2203',
                    'SUPERERBUINO3_2203',
                    'SUPERERBUINO4_2203',
                    'SUPERERBUINO5_2203',
                    'SUPERERBUINO6_2203',
                    'SUPERERBUINO7_2203'
                    ]:
        return 'SUPERMERCADOS EBURNIO CORREA'    

    elif valor in ['SUPERMELLO_2203',
                    'MELLOSILVA_2203',
                    'SUPERBIG_2203',
                    'SBSUPER_2203',
                    'CSBSUPER_2203',
                    'GIGANTE_2203',
                    'CASHCARRY_2203',
                    ]:
        return 'SUPER MELLO ATACADISTA DE ALIME'    
    
    elif valor in ['RFELICETTI_2203', 'SFELICETTI_2203']:
        return 'RESTAURANTE FELICETTI LTDA'
    
    elif valor in ['FRANK_2203']:
        return 'FRANCK F MULLER SUPERMERCADOS'    


    else:
        return valor
