class MultiClassHelper():
    def get_class_dict(self, classes):
       dct = {}
       idx = 0
       for cls in classes:
           if not cls in dct:
               dct[cls] = idx
               idx += 1
       return dct, idx

