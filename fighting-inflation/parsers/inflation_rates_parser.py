def parse_inflation_rates_download():

    with open('in/csv/inflation_rates/bna_data.csv', 'r') as download_data,\
            open('in/csv/inflation_rates/inflation_rates.csv', 'w') as rates_file:

        rates_file.write('month,rate\n')

        for line in download_data:
            line = line.strip().split(';')
            line[0] = line[0][3:]
            line[1] = line[1].replace(',', '.')
            line = ','.join(line)
            rates_file.write(line + '\n')
