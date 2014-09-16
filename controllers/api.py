@request.restful()
def services():
    response.view = 'generic.json'
    
    def GET(*args,**vars):
        search_by_id = False

        pattern = [
            "/stores[stores]",
            "/articles/stores/{articles.store_id}",
            "/articles[articles]"
            ]

        if len(args) >= 3:
            search_by_id = True
            if not args[-1].isdigit():
                return dict(success= False, error_code='400', error_msg='Bad request')
                pass
            pass

        parser = db.parse_as_rest(pattern,args,vars)
        name = args[0]

        if parser.status == 200:
            obj = parser.response
            if search_by_id and len(obj)==0:
                return dict(success= False, error_code='404', error_msg='Record not Found')
                pass
            dictionary= {'success':True, name:obj, 'total_elements':len(obj)}
            return dictionary
        elif parser.status == 500:
            return dict(success= False, error_code=parser.status, error_msg='Server Error')
        else:
            return dict(success= False, error_code=parser.status, error_msg=parser.error)
    return locals()

