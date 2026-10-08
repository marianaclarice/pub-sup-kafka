# Atividade novo tópico no projeto pub-sub

Gerei uma senha de app no Gmail<br>
Criei o arquivo .env para guardar as credenciais de senha app + email remetente + email destinatário.<br>
Editei os arquivos rotate e grayscale para publicarem em notificacao. <br>
Ajustei o docker-compose.yml<br>
<br>
## Problemas encontrados:
Comecei pelo VsCode local, mas durante a subida do Docker, os containers não iniciavam devido à falta de espaço no disco. A solução foi migrar o ambiente para o Code-Server e lá, depois de algumas primeiras tentativas ainda tendo problema com espaço, expandi o armazenamento da instância EC2 de 8 GB para 20 GB.
<br>
<img width="1917" height="862" alt="Captura de tela 2026-10-07 215511" src="https://github.com/user-attachments/assets/12cf4f41-64a3-4770-ac39-59f8dc22ec37" />
<img width="1623" height="362" alt="Captura de tela 2026-10-07 215050" src="https://github.com/user-attachments/assets/eefe8714-0da3-4dfa-9841-8e25143ffcae" />
