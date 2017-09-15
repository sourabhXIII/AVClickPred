
class DataExploration:

    @staticmethod
    def explore_data(df):
        # have a glimpse of the data
        # print(df.head(5))

        # print the total number of rows and columns
        print("#Rows = %s, #Columns = %s" % (len(df),  len(df.columns)))
        for col in df.columns:
            # print column-wise details
            print("About %s ::" % col)

            # check whether any missing values are there or not
            print("     #Missing/NaN values = %s" % df[col].isnull().sum())

            # check column wise unique value count
            print("     #Unique values = %s" % (len(df[col].unique())))
