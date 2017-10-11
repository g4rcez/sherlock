# Implementações: Sherlock

- Limpeza de informações em tela

- Melhoria de Layout Web

- Armazenamento em um diretório de acordo com o site informado. Padrão: **sherlock_$site_$numero**

- Tradução de mensagens em tela, com base nos arquivos de configuração. Modelo:

```json
{
  "extensions": [],
  "idioma": "pt-br",
  "html": "",
  "json": "",
  "referer": [],
  "limit": "",
  "whois": "",
}
```

- Refatoração de código. Metas a seguir:
1. Tratamento de Excessões
2. Extração de métodos, de acordo com as configurações e parâmetros passados
3. Reduzir o total de requisições feitas ao decorrer do programa.
4. Obter filtragens de lista, reduzindo redundâncias.

- Fluxo de informações:

1. Listar páginas através dos códigos 200, 403 e 500.
2. Listar páginas internas com 404.
3. Relacionar links externos com o domínio
4. Obter informações whois e afins.
5. Localização física e precisas (via CEP e ZipCode)

- Versões Futuras
1. Identificação de formulários administrativas, cadastrais e de usuários (pt-br e en)
2. Identificação específica de redes sociais
3. Identificação de telefones e celulares
