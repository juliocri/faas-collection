def combinatory(event, context):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    output = [a + b +c + d for a in letters for b in letters for c in digits for d in digits]
    return "Combined!"
