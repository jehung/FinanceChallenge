import numpy as np
import pandas as pd



def get_data():
    dir = 'D:\\Backups\\StemData\\'
    #file_list = ['sample_orig_2016.txt', 'sample_svcg_2016.txt']
    file = 'sample_orig_2016.txt'
    file1 = 'sample_svcg_2016.txt'

    raw = pd.read_csv(dir+file, sep='|', header=None)
    raw.columns = ['credit_score', 'first_pmt_date', 'first_time', 'mat_date', 'msa', 'mi_perc', 'units',
                    'occ_status', 'ocltv', 'odti', 'oupb', 'oltv', 'oint_rate', 'channel', 'ppm', 'fixed_rate',
                    'state', 'prop_type','zip','loan_num', 'loan_purpose','oterm','num_borrowers', 'seller_name',
                    'servicer_name','exceed_conform']

    raw1 = pd.read_csv(dir+file1, sep='|', header=None)
    raw1.columns = ['loan_num', 'yearmon', 'curr_upb','curr_delinq','loan_age','remain_months', 'repurchased',
                     'modified', 'zero_bal','zero_date','curr_rate','curr_def_upb', 'ddlpi','mi_rec','net_proceeds',
                     'non_mi_rec', 'exp', 'legal_costs','maint_exp','tax_insur', 'misc_exp', 'loss','mod_exp']

    data = pd.merge(raw, raw1, on='loan_num', how='inner')
    subdata = data.sample(50000, random_state=100)

    return subdata



ans = get_data()
print(ans.shape)
