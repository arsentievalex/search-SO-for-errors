import requests
import webbrowser


def func_to_test():  # replace with your function
    x = 'test' + 5
    return x


try:
    func_to_test()

except Exception as e:
    e = str(e)
    print("Searching for " + e)
    # get json response from stack exchange API
    resp = requests.get("https://api.stackexchange.com/"+"/2.3/search/advanced?order=desc&sort=votes&accepted=True&title={}&site=stackoverflow".format(e))
    json = resp.json()

    # if the response json is not empty then fetch the first url and open it in browser
    if len(json['items']) > 0:
        url = json['items'][0]['link']
        webbrowser.open(url)
    else:
        print('Error not found on SO')
