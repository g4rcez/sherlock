# Manual do Usuário

**Sherlock** possui uma pequena lista (que tende a crescer) de parâmetros para
seu uso. Você pode observar melhor na tabela abaixo:

<pre>
Parâmetro     Valor
-b, --both        Atribui uma wordlist e os links buscados nas páginas

-e, --extensions  Extensões de arquivos a serem indexados* (em desenvolvimento)

-j, --json        Gerar arquivo Json das informações capturadas (deve informar o nome do arquivo)

-h, --help        Menu de ajuda ao usuário (Mostrado caso 3 ou menos argumentos sejam passados)

-H, --html        Gera páginas HTML referentes a busca feita no domínio (exige nome de um diretório)

-l, --limit       Limite de requisições feitas até uma pausa.

-L, --language	  'Accept-Language' do cabeçalho HTTP. Pode ser passado mais de um locale, separado por vírgula ','

-r, --referer	    'Referer' do cabeçalho HTTP. Pode ser passado mais de um referer, separado por vírgula ','

-s, --subdomain   Realiza tentativas de subdominio(parâmetro -w obrigatório)

-t, --target      Página raiz do site a ser analisado.

-w, --wordlist    Wordlist para tentativa de bruteforce

-W, --whois       Wordlist para tentativa de bruteforce
</pre>

\*Extensões reconhecidas pelo programa:
> jpg, jpeg, pdf, png, mp3, mp4, avi, docx, doc, odt, txt,gif, js, css, csv,
exe, mov, psd, tar, zip, wav, xml, xsl, ppt, pptx, m4a, ogg, m4v, ogv,
3gp, mpg, 3gp, xls

- **Language** e **Referer** são utilizados para a forja de um cabeçalho HTTP fake, a cada nova requisição,
por padrão, um 'User-Agent' diferente é utilizado.
