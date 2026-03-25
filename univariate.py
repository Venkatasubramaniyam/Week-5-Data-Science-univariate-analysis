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