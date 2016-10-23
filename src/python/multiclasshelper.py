class MultiClassHelper():
    def get_class_dict(self, classes):
       dct = {}
       idx = 0
       for cls in classes:
           if not cls in dct:
               dct[cls] = idx
               idx += 1
       return dct, idx

    def classes_to_array(self, classes, dct):
        a = [0 for i in range(len(dct))]
        for cls in classes:
            if cls in dct:
                idx = dct[cls]
                a[idx] = 1
        return a

