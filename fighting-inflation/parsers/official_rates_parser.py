def parse_bna_rates_download():

    with open('in/csv/official_rates/bna_data.csv', 'r') as download_data,\
            open('in/csv/official_rates/official_rates.csv', 'w') as rates_file:

        # ignore download header
        download_data.readline()
        rates_file.write('date,buy,sell\n')

        for line in download_data:
            line = line.strip()[:-1].split(';')
            line[1], line[2] = line[1].replace(
                ',', '.'), line[2].replace(',', '.')
            line = ','.join(line)
            rates_file.write(line + '\n')
