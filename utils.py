import sys
import glob
import serial


def list_serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def string_to_list(input_str):
    # convert a string to set
    if ',' in input_str:
        str_buf = input_str.split(',')
        return [x.strip() for x in str_buf]
    else:
        return [input_str]

def list_to_string(input_list):
    if len(input_list) == 0:
        return ''
    elif len(input_list) == 1:
        return input_list[0]
    # more than 1 element
    ret_str = ''
    for i in range(len(input_list) - 1):
        ret_str += input_list[i] + ', '
    ret_str += input_list[-1]
    return ret_str


if __name__ == '__main__':
    print(list_serial_ports())