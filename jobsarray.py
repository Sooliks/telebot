import array
class JobsArray:
    def maximum(self,array):
        max=array[0]
        for i in range(len(array)):
            if array[i]>max:
                max=array[i]
        return max