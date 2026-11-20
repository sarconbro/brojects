def time_string_split(time_string):          # time_str in int und str zerlegen
    time_split = time_string.split(":")
    return int(time_split[0]), time_split[1]      # hours(int), minutes(str) für convert

def add_hours_to_gmt4(h):                 # gmt+0 zu gmt+4 durch addition zu hour(int)
    return (h + 4) % 24                             # modulo 24 wegen 24h-format bei mitternachtsprung, new_hours für convert

def convert_to_gmt_plus_4(time_str):         # main function, combines alle oben
    hours, minutes = time_string_split(time_str)    # time_strg_split function; hours(int), minutes(str
    new_hours = add_hours_to_gmt4(hours)            # add_hours function; new_hours(int)
    return f"{str(new_hours).zfill(2)}:{minutes}"   # gmt+4 final result als str, f-string zero padding "0"2:34 bei einstelliger hour

print(convert_to_gmt_plus_4("14:34"))
print(convert_to_gmt_plus_4("22:34"))