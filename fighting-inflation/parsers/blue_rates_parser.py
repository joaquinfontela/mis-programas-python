def parse_blue_rates_download():

    with open('in/csv/blue_rates/ambito_data.csv', 'r') as download_data,\
            open('in/csv/blue_rates/blue_rates.csv', 'w') as rates_file:

        rates_file.write('date,buy,sell\n')

        lines = []
        for line in download_data:
            line = line.strip().split(';')
            line[1], line[2] = line[1].replace(
                ',', '.'), line[2].replace(',', '.')
            line = ','.join(line)
            lines.append(line + '\n')

        rates_file.writelines(lines[::-1])
