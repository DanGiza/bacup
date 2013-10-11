import requests
import webbrowser
import logging
import simplejson as json
# Legend
# Start of var: str-string, nr-number, pw-password!,
# End of var: l-link, t-text, o-object
#

logging.basicConfig(level = logging.INFO)

class BOX:
    """
    www.box.com api
    works:
        ->  login
        ->  get token w/ error handling
    to-do:
        ->  upload/download/explore
    """

    str_BuildGet        = 'https://www.box.com/api/oauth2/authorize?'
    str_redirect_uri    = 'https://www.box.com/developers/services'
    str_response_type   = 'response_type=code'
    str_state           = 'authenticated'
    str_BuildToken      = 'https://www.box.com/api/oauth2/token'
    str_client_id       = 'j11v31md50xohags558ue1t2bteto63w'
    str_client_secret   = 'awHdRpTm7eMslhv4ZelwxT81GIhHsXV2'
    str_grant_type      = 'authorization_code'
    str_code            = ''

    def __init__(self):
        self.str_BuildGet = self.str_BuildGet + self.str_response_type + '&' + 'client_id=' + self.str_client_id + '&' + 'state=' + self.str_state
        self.str_code = raw_input('Enter code parameter (code=something) from URL: ')

    def GetCODE(self):
        webbrowser.open_new_tab(self.str_BuildGet)

    def GetTOKEN(self):
        """
        returns 2 parameters:
        1 -> 0/1 : nok/ok
        2 -> server response
        """
        payload_GetRequest = {'grant_type'      : self.str_grant_type,
                              'code'            : self.str_code,
                              'client_id'       : self.str_client_id,
                              'client_secret'   : self.str_client_secret}
        o_MyRequest = requests.post(self.str_BuildToken, data = payload_GetRequest)

        try:
            responseDict = json.loads(o_MyRequest.text)
        except Exception as err:
            print 'ERROR at handling POST response data: \n' % err
            return 0, o_MyRequest.text

        try:
            if responseDict['access_token']:
                return 1, responseDict
        except Exception as err:
            # print 'ERROR:GetTOKEN() -> POST response:\n' % err
            log
            return 0, o_MyRequest.text

    def BOX_LogIn(self):
        self.GetCODE()
        errorCode, response = self.GetTOKEN()
        if errorCode == 1:
            return
        else:
            print 'ERROR:GetTOKEN() -> POST response:\n' % response
