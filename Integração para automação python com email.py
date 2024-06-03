# %%
import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'remetente' # meu email
    msg['To'] = 'destinatario'# se for mais de uma pessoa,separapor virgula
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:



# %%
import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto" # Tema do e-mail
    msg['From'] = 'lcolares91@gmail.com' # meu email
    msg['To'] = 'lcolares91@gmail.com'# se for mais de uma pessoa,separapor virgula

    password = 'npqlssriosywikia' 
    # Vai gerenciar a conta e criar uma senha própia para essa ação,após isso só aplicar essa senha(Vai logar normal na sua conta,por um dia)
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()






