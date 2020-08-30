from sklearn.base import BaseEstimator, TransformerMixin

class AddProfileNumber(BaseEstimator, TransformerMixin):       
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()        
        data = data.assign(PROFILENUMERICO=data["PROFILE"].map({'beginner_front_end': 7, 'advanced_front_end': 1, 'beginner_backend': 3, 'advanced_backend': 4, 'beginner_data_science': 5, 'advanced_data_science': 6}))
        return data
# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
	# pus
        return data.drop(labels=self.columns, axis='columns')
