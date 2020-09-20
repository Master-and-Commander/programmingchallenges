from weasyprint import HTML, CSS

# https://weasyprint.readthedocs.io/en/stable/tutorial.html

def returnSampleQuestion(first, second, operator):
    htmlstring ='''
    <div>
    <div class = 'generalmath'>
      <div class='operator'>
        ''' + operator + '''
      </div>
      <div class='numbers'>
        <div class='first'>
        ''' + first + '''
        </div>
        <div class='second'>
        ''' + second + '''
        </div>
      </div>

    </div>
    <hr class = 'hrgeneral'/>
    </div>
    '''

    return htmlstring


def returnPDF(name,cssstring):
    htmlstring = "<h1>" + name + "</h1>"
    htmlstring = htmlstring + returnSampleQuestion("5", "10", "*")
    html = HTML(string=htmlstring)
    css = CSS(string=cssstring)
    html.write_pdf(
    'example3.pdf', stylesheets=[css])

cssstring ='''
    .generalmath {
        display:block;
        width: 50px;
        height:50px;

    }
    .hrgeneral {
      width: 30px;
      margin-left: 0px;
      padding: 0px;
    }
    .operator {
      color: red;
      font-size: 200%;
      float:left;

    }
    .numbers {
      color: green;
      float:right;
      padding:0px;
      display:block;
      margin-right:auto;
    }
    .first {

    }
    .second {

    }
'''

returnPDF("Weasy print test", cssstring)
