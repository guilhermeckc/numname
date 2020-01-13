unique = {1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove",
          10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
          17: "dezessete", 18: "dezoito", 19: "dezenove", 100: "cem", 0: "zero"}
dozens = {2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta", 8: "oitenta",
          9: "noventa"}
hundreds = {1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos",
            7: "setecentos", 8: "oitocentos", 9: "novecentos"}


def get_unit(num):
    name = unique[int(num)]
    return name


def get_dozens(num):
    int_num = int(num)
    if int_num > 9:
        tag1, tag2 = int(num[0]), int(num[1])
        if int_num in unique.keys():
            name = unique[int_num]
        else:
            if tag2 == 0:
                name = dozens[tag1]
            else:
                name = dozens[tag1] + ' e ' + unique[tag2]
    else:
        name = unique[int_num]
    return name


def get_hundreds(num):
    int_num = int(num)
    tag1, tag2 = int(num[0]), int(num[1:])
    try:
        name = unique[int_num]
    except:
        if tag1 == 0:
            name = get_dozens(str(tag2))
        else:
            if tag2 == 0:
                name = hundreds[tag1]
            else:
                name = hundreds[tag1] + ' e ' + get_dozens(str(tag2))
    return name


def number_name(key):
    if '.' in key:
        final_name = "You must provide a integer number."
    else:
        try:
            key = int(key)
            if key in range(-99999, 100000):
                first_tag = ''
                if key >= 0:
                    absolute = key
                else:
                    absolute = key * (-1)
                    first_tag = 'menos '
                nstr = str(absolute)
                if len(nstr) == 5:
                    tag1, tag2 = nstr[:2], nstr[2:]
                    if tag2 == '000':
                        final_name = get_dozens(tag1) + ' mil'
                    else:
                        final_name = get_dozens(tag1) + ' mil' + ' e ' + get_hundreds(tag2)
                elif len(nstr) == 4:
                    tag1, tag2 = nstr[0], nstr[1:]
                    if tag2 == '000':
                        final_name = get_unit(tag1) + ' mil '
                    else:
                        final_name = get_unit(tag1) + ' mil e ' + get_hundreds(tag2)
                elif len(nstr) == 3:
                    final_name = get_hundreds(nstr)
                elif len(nstr) == 2:
                    final_name = get_dozens(nstr)
                elif len(nstr) == 1:
                    final_name = get_unit(nstr)
                else:
                    final_name = "Sorry! Something is wrong. Please, contact site manager."
                final_name = {key: first_tag + final_name}
            else:
                final_name = "This number is out of range [-99999, 99999]"
        except:
            final_name = "You must provide a integer number."
    return final_name
