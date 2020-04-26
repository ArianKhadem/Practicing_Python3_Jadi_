def Input_function_maker (name_of_function, number_of_def_arguments, arguments) :
    NAME = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG']
    if number_of_def_arguments >= 6 :
        number_of_def_arguments = 6
    for i in (1, number_of_def_arguments) :
        if type(arguments) == str :
           print('def',name_of_function,'() :')
               
        # elif type(arguments) == int :
        #     def name_of_function(i) :
                
        # elif arguments == 'float' :
        #     def name_of_function(i) :
                
        # elif arguments == 'Boolean' :
        #     def name_of_function(i) :
                
        # elif arguments == 'ascii' :
        #     def name_of_function(i) :
                
        # elif arguments == 'bin' :
        #     def name_of_function(i) :
                
        # elif arguments == 'chr' :
        #     def name_of_function(i) :
        
Input_function_maker('testing', 3, 'str')