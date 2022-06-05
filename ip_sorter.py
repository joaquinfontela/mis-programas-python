def sort_ips(ips):
    return ['.'.join([str(val) for val in num_ip]) for num_ip in sorted([[int(val)
                                                                          for val in ip.split('.')] for ip in ips])]


print(sort_ips(['114.24.76.87', '23.76.1.12', '23.71.65.77',
                '12.114.166.34', '114.24.76.86']))
