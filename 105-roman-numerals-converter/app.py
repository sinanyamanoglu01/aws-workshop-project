from flask import Flask, render_template, request

app = Flask(__name__)

# 1-I 
# 2-II
# 3-III
# 4-IV
# 5-V
# 6-VI
# 7-VII
# 8-VIII
# 9-IX
# 10-X
# 1-3999
def convert(decimal_num):
    roman = {1000: 'M', 900:'CM', 500:'D', 400: 'CD', 100: 'C', 90:'XC', 50:'L', 40: 'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

    num_to_roman=''

    for i in roman.keys():
        # 'M' * (1994 // 1000) --> 'M'*1 --> M  
        num_to_roman += roman[i] * (decimal_num // i)
        # decimal_num = decimal_num % i
        # 1994 %= 1000 --> 994 --> decimal_num = 994
        decimal_num %= i
    return num_to_roman


# 13 cycle... 
# 1 -- M
# 2 -- MCM
# 3-5 -- MCM
# 6 -- MCMXC
# 7-11 -- MCMXC
# 12 -- MCMXCIV
# 13 -- MCMXCIV
# print('1994 -- ', convert(1994))

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', not_valid=False, developer_name='Callahan')

@app.route('/', methods=['POST'])
def main_post():
    alphanumeric = request.form['alpha']
    if not alphanumeric.isdecimal():
        return render_template('index.html', not_valid=True, developer_name='Callahan')
    number=int(alphanumeric)
    if not (0 < number < 4000):
        return render_template('index.html', not_valid=True, developer_name='Callahan')
    return render_template('result.html', number_decimal=number, number_roman=convert(number), developer_name='Callahan' )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)









