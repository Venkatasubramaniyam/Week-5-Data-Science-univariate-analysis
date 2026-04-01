class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnname in dataset.columns:
            if (dataset[columnname].dtypes=='str'):
                qual.append(columnname)
            else:
                quan.append(columnname)
        return quan,qual

    def univariate(quan,dataset):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater",
                                        "min","max","skew","kurtosis","var","std"],columns=quan)
        for columnname in quan:
            descriptive.loc["Mean",columnname]=dataset[columnname].mean()
            descriptive.loc["Median",columnname]=dataset[columnname].median()
            descriptive.loc["Mode",columnname]=dataset[columnname].mode()[0]
            descriptive.loc["Q1:25%",columnname]=dataset.describe()[columnname]["25%"]
            descriptive.loc["Q2:50%",columnname]=dataset.describe()[columnname]["50%"]
            descriptive.loc["Q3:75%",columnname]=dataset.describe()[columnname]["75%"]
            descriptive.loc["99%",columnname]=np.percentile(dataset[columnname],99)
            descriptive.loc["Q4:100%",columnname]=dataset.describe()[columnname]["max"]
            descriptive.loc["IQR",columnname]=descriptive.loc["Q3:75%",columnname]-descriptive.loc["Q1:25%",columnname]
            descriptive.loc["1.5rule",columnname]=1.5*descriptive.loc["IQR",columnname]
            descriptive.loc["Lesser",columnname]=descriptive.loc["Q1:25%",columnname]-descriptive.loc["1.5rule",columnname]
            descriptive.loc["Greater",columnname]=descriptive.loc["Q3:75%",columnname]+descriptive.loc["1.5rule",columnname]
            descriptive.loc["min",columnname]=dataset[columnname].min()
            descriptive.loc["max",columnname]=dataset[columnname].max()
            descriptive.loc["skew",columnname]=dataset[columnname].skew()
            descriptive.loc["kurtosis",columnname]=dataset[columnname].kurtosis()
            descriptive.loc["var",columnname]=dataset[columnname].var()
            descriptive.loc["std",columnname]=dataset[columnname].std()
        return descriptive

    def freq_table(columnname,dataset):
        freq_table=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","Cumsum"])
        freq_table["Unique_values"]=dataset[columnname].value_counts().index
        freq_table["Frequency"]=dataset[columnname].value_counts().values
        freq_table["Relative_Frequency"]=freq_table["Frequency"]/103
        freq_table["Cumsum"]=freq_table["Relative_Frequency"].cumsum()
        return freq_table

    def findoutlier():
        lesser=[]
        greater=[]
        for columnname in quan:
            if (descriptive.loc["min"][columnname]<descriptive.loc["Lesser"][columnname]):
                lesser.append(columnname)
            if (descriptive.loc["max"][columnname]>descriptive.loc["Greater"][columnname]):
                greater.append(columnname)
        return lesser,greater

    #replacing outlier values, so no oulier present
    def replaceoutlier():
        lesser=[]
        greater=[]
        for columnname in lesser:
            dataset.loc[dataset[columnname] < descriptive.loc["Lesser", columnname],columnname] = descriptive.loc["Lesser", columnname]
        for columnname in greater:
            dataset.loc[dataset[columnname] > descriptive.loc["Greater", columnname],columnname] = descriptive.loc["Greater", columnname]
        return lesser,greater
    
    