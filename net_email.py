from poplib import POP3
import email
import email.header


def decode_email_content(msg_src,names):
    msg = email.message_from_bytes(msg_src)
    result = {}
    for name in names:
        content = msg.get(name)
        info = email.header.decode_header(content)
        if info[0][1]:
            # 已知编码
            if info[0][1].find('unknown-') == -1:
                result[name] = info[0][0].decode(info[0][1])
            else:
                try:
                    result[name] = info[0][0].decode('utf-8')
                except:
                    pass
        else:
            result[name] = info[0][0]
    return result


if __name__ == '__main__':
    pp = POP3('pop3.163.com')
    pp.user('1101202419@qq.com')
    pp.pass_('')
    total,totalnum = pp.stat()
    print(total,totalnum)


