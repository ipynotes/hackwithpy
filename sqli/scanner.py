import mechanize


url = input("Enter the full url")
   attack_no = 1

With open ('vectors.txt') as v:
    For line in v:
        browser.open(url)
        browser.select_form(nr = 0)
        browser["id"] = line
        res = browser.submit()
        content = res.read()
        print ("Attack {}".format(attack_no))
        print (content)
