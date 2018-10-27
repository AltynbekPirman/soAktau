import re


class PhoneLinker:

    mobile_operator_codes = (
        '700', '701', '702', '705', '707', '708', '712', '713', '717', '718', '721', '725', '726', '778',
        '727', '747', '750', '751', '760', '761', '762', '763', '764', '771', '775', '776', '777',
    )
    regex_str = '|'.join(['({})']*len(mobile_operator_codes)).format(*mobile_operator_codes)
    regex = re.compile(r'(^|\s)(\+7|8( )?)({})( )?((\d\d\d\d\d\d\d)|(\d\d\d-\d\d-\d\d)|(\d\d\d-\d\d\d\d)|(\d\d\d \d\d \d\d)'
                       r'|(\d\d\d \d\d\d\d))'.format(regex_str), re.I)

    def __init__(self, text):
        self.text = text

    def _find_phones(self) -> tuple:
        return tuple(self.regex.finditer(self.text))

    def href_phones(self):
        i = 0
        output = ''
        if self._find_phones():
            for phone in self._find_phones():
                if self.text[phone.start()] == " ":
                    tel_num = self.text[(phone.start()+1):phone.end()]
                    tel_num = self._extract_number(tel_num)
                    output += ''.join((self.text[i:phone.start()+1], '<a href="tel:{}">'.format(tel_num),
                                       self.text[(phone.start()+1):phone.end()], '</a>'))
                else:
                    tel_num = self.text[phone.start():phone.end()]
                    tel_num = self._extract_number(tel_num)
                    output += ''.join((self.text[i:phone.start()], '<a href="tel:{}">'.format(tel_num),
                                       self.text[phone.start():phone.end()], '</a>'))
                i = phone.end()

            highlighted_text = "".join([output, self.text[phone.end():]])
            return highlighted_text
        return self.text

    @staticmethod
    def _extract_number(phone: str) -> str:
        res = ''
        for char in phone:
            if char.isdigit() or char == "+":
                res += char
        return res


class ImageLinker:

    regex = re.compile('<img src="/media/django-summernote')
    _host_addr = 'http://0.0.0.0:2003'

    def __init__(self, text):
        self.text = text

    def link_images(self) -> str:
        i = 0
        output = ''
        if self._find_images():
            for image in self._find_images():
                output += ''.join((self.text[i:image.start() + 10], str(self._host_addr),
                                   self.text[(image.start() + 10):image.end()]))
                i = image.end()

            highlighted_text = "".join([output, self.text[image.end():]])
            return highlighted_text
        return self.text

    def _find_images(self) -> tuple:
        return tuple(self.regex.finditer(self.text))


if __name__ == '__main__':
    # text = '+7702 969-15-95 87759691595'
    # text = 'fdgf +77750 dfds'
    # a = PhoneLinker(text).href_phones()
    # a = PhoneLinker._extract_number('+7702 969-15-95')
    # print(a)

    a = '<p>fgghfhgf jhg jhg jhgjhghj&nbsp;&nbsp;<img src="/media/django-summernote/2018-10-27/9f91375d-e00f-4a15-b4f2-9252f5108e1b.png" ' \
    'style="width: 271px;"></p>'
    print(ImageLinker(a).link_images())
