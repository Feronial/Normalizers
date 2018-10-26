 # code returns list that contains [month -2 , month -1 , month, month + 1]
 
 def month_Normalizer(month):
        
        
        date_List = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        
        
        if month == 1:
            
            result_List = [date_List[month-3],date_List[month-2],date_List[month],date_List[month + 1]]
                
        elif month == 2:
            
            result_List = [date_List[month-3],date_List[month-1],date_List[month],date_List[month + 1]]
            
        elif month == 12:
            
            result_List = [date_List[month-2],date_List[month-1],date_List[month],date_List[(month + 1)%12]]
        else:
            
            result_List = [date_List[month-2],date_List[month-1],date_List[month],date_List[month + 1]]
        
        return result_List
