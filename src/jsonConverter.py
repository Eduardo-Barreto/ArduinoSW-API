import json

path = './examples/jsonConverter'
in_file = json.load(open(f'{path}/in.json', 'r', encoding='utf-8'))
out_file = open(f'{path}/out.json', 'w', encoding='utf-8')
board = in_file['UNO']

out_dict = {}

for port_name in board:
    port = board[port_name]
    for bit_name in port:
        bit = port[bit_name]
        for pin_name in bit:
            out_dict[pin_name] = {
                'wPort': f'PORT{port_name}',
                'rPort': f'PIN{port_name}',
                'bit': bit_name,
            }


out_file.write(json.dumps(out_dict))
