import pandas as pd
mod=pd.read_csv('clear_data/df_models.csv')
mat=pd.read_csv('clear_data/df_materials.csv')
alfa=mod.merge(mat[['mini','faction']],on='mini',how='left')
mask=alfa['faction'].isna()
names=alfa[mask]['mini'].tolist()
print(f'Total NaN: {len(names)}')
for n in names:
    print(n)
