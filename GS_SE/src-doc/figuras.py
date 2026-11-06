# -*- coding: utf-8 -*-
"""Figuras da GS2026.2 — Neighborhood Action Dashboard (Engenharia de Software)."""
import math
from svgbase import Tela, CORES


def bloco(t, x, y, w, h, titulo, tecnologia, desc, cor, tam=14):
    t.caixa(x, y, w, h, cor=cor, r=8)
    tl = titulo.split("\n")
    for i, l in enumerate(tl):
        t.texto(x + w / 2, y + 26 + i * 19, l, tam=tam, peso="bold", anc="middle")
    dy = (len(tl) - 1) * 19
    if tecnologia:
        t.texto(x + w / 2, y + 46 + dy, "[%s]" % tecnologia, tam=11.5, anc="middle",
                cor="#444444")
    y0 = y + dy + (66 if tecnologia else 48)
    for i, l in enumerate(desc.split("\n")):
        t.texto(x + w / 2, y0 + i * 17, l, tam=12, anc="middle", cor="#333333")


# =============================================================== figura 1
def c4_contexto():
    t = Tela(1280, 760)

    t.retangulo(420, 300, 440, 180, fundo="#dff0e4", borda="#1e6b3a", traco=2.8, r=14)
    t.texto(640, 346, "Neighborhood Action", tam=21, peso="bold", anc="middle",
            cor="#1e6b3a")
    t.texto(640, 374, "Dashboard", tam=21, peso="bold", anc="middle", cor="#1e6b3a")
    t.texto(640, 398, "[Sistema de software]", tam=12, anc="middle", cor="#444444")
    t.paragrafo(640, 424, [
        "Registra, organiza, prioriza e acompanha",
        "demandas de melhoria do bairro, com",
        "transparência para o cidadão.",
    ], tam=12, anc="middle", cor="#222222")

    atores = [
        (60, "Cidadão", "Registra demandas, informa\nlocalização e acompanha"),
        (280, "Gestor Público", "Analisa, prioriza, atualiza\nsituação e encerra"),
        (500, "Administrador", "Gerencia usuários, categorias\ne configurações"),
    ]
    for y, nome, desc in atores:
        t.retangulo(40, y, 300, 110, fundo="#ebebeb", borda="#3f3f3f", traco=2.2)
        t.texto(190, y + 32, nome, tam=16, peso="bold", anc="middle")
        for i, l in enumerate(desc.split("\n")):
            t.texto(190, y + 58 + i * 18, l, tam=12.5, anc="middle", cor="#444444")

    t.seta(344, 112, 416, 330)
    t.texto(366, 196, "registra e", tam=11.5, cor="#555555")
    t.texto(366, 212, "acompanha", tam=11.5, cor="#555555")
    t.seta(344, 334, 416, 362)
    t.texto(352, 318, "prioriza e atualiza", tam=11.5, cor="#555555")
    t.seta(344, 554, 416, 450)
    t.texto(352, 520, "configura", tam=11.5, cor="#555555")

    externos = [
        (40, "Serviço de Mapas e\nGeocodificação", "converte endereço em coordenada\ne desenha o mapa do bairro"),
        (190, "Provedor de Identidade\n(gov.br)", "autenticação do cidadão\ne do gestor público"),
        (340, "Sistema de Protocolo\nda Prefeitura", "integra a demanda ao fluxo\noficial de atendimento"),
        (490, "Serviço de Notificação\n(e-mail e push)", "informa o cidadão a cada\nmudança de situação"),
        (640, "Armazenamento de\nMídias", "guarda as fotos enviadas\njunto da ocorrência"),
    ]
    for y, nome, desc in externos:
        t.retangulo(940, y, 300, 108, fundo="#eaf2fb", borda="#1f4e79", traco=2.2)
        ls = nome.split("\n")
        for i, l in enumerate(ls):
            t.texto(1090, y + 28 + i * 19, l, tam=13.5, peso="bold", anc="middle",
                    cor="#1f4e79")
        for i, l in enumerate(desc.split("\n")):
            t.texto(1090, y + 28 + len(ls) * 19 + 8 + i * 16, l, tam=11.5,
                    anc="middle", cor="#444444")
        t.seta(864, 390, 936, y + 54)

    t.texto(40, 700, "Pessoas", tam=13, peso="bold")
    t.texto(940, 700, "Sistemas externos", tam=13, peso="bold")
    t.texto(640, 730, "C4 — Nível 1: diagrama de contexto. As setas indicam a "
            "finalidade de cada interação.", tam=12.5, anc="middle", italico=True,
            cor="#555555")
    return t.salvar("fig_c4_contexto")


# =============================================================== figura 2
def c4_containers():
    t = Tela(1300, 860)

    t.retangulo(380, 108, 800, 640, fundo="#fbfbfb", borda="#1e6b3a", traco=2.4,
                r=12, tracejado="10 6")
    t.texto(780, 136, "Neighborhood Action Dashboard", tam=15, peso="bold",
            anc="middle", cor="#1e6b3a")

    bloco(t, 420, 160, 320, 104, "Portal Web", "React, SPA",
          "cidadão registra e acompanha;\ngestor prioriza e encerra", "azul")
    bloco(t, 820, 160, 320, 104, "Aplicativo Móvel", "React Native",
          "registro em campo com foto\ne localização do aparelho", "azul")

    bloco(t, 520, 320, 500, 112, "API de Demandas", "Node.js com NestJS · REST/JSON",
          "adaptadores de entrada e núcleo de domínio hexagonal:\n"
          "registro, priorização, situação e consulta", "verde")

    bloco(t, 420, 486, 300, 100, "Serviço de Notificações", "worker Node.js",
          "consome eventos e avisa\no cidadão a cada mudança", "ocre")
    bloco(t, 840, 486, 300, 100, "Agregador de Indicadores", "worker Node.js",
          "consolida o painel por bairro,\ncategoria e tempo de resolução", "ocre")

    bloco(t, 420, 630, 300, 94, "Banco de Dados", "PostgreSQL + PostGIS",
          "ocorrências, usuários, categorias\ne consultas por área", "lilas")
    bloco(t, 840, 630, 300, 94, "Fila de Mensagens", "RabbitMQ",
          "desacopla o registro das\nnotificações e dos indicadores", "lilas")

    ext = [
        (40, 170, "Provedor de\nIdentidade (gov.br)", 340),
        (40, 290, "Serviço de Mapas e\nGeocodificação", 365),
        (40, 410, "Armazenamento de\nMídias (objetos)", 390),
        (40, 530, "Sistema de Protocolo\nda Prefeitura", 415),
    ]
    for x, y, nome, alvo in ext:
        t.retangulo(x, y, 190, 86, fundo="#eaf2fb", borda="#1f4e79", traco=2)
        for i, l in enumerate(nome.split("\n")):
            t.texto(x + 95, y + 36 + i * 19, l, tam=12.5, peso="bold", anc="middle",
                    cor="#1f4e79")
        t.seta(234, y + 43, 516, alvo)

    t.paragrafo(40, 676, [
        "Integrações em HTTPS/JSON, sempre",
        "através do adaptador de saída",
        "correspondente — nunca a partir",
        "do núcleo de domínio.",
    ], tam=11.5, cor="#555555", dy=17)

    t.seta(580, 268, 660, 316)
    t.texto(500, 300, "HTTPS/JSON", tam=11.5, cor="#555555")
    t.seta(980, 268, 900, 316)
    t.texto(990, 300, "HTTPS/JSON", tam=11.5, cor="#555555")

    t.seta(660, 436, 580, 482)
    t.texto(452, 470, "publica evento", tam=11.5, cor="#555555")
    t.seta(900, 436, 980, 482)
    t.texto(992, 470, "publica evento", tam=11.5, cor="#555555")

    t.seta(570, 586, 570, 626)
    t.texto(582, 612, "SQL/TLS", tam=11.5, cor="#555555")
    t.seta(990, 586, 990, 626)
    t.texto(1002, 612, "AMQP", tam=11.5, cor="#555555")
    t.linha(720, 676, 840, 676, cor="#666666", larg=2.0, tracejado="7 5")
    t.texto(780, 666, "consome", tam=11.5, anc="middle", cor="#555555")

    t.seta(780, 432, 780, 626)
    t.texto(792, 540, "SQL/TLS", tam=11.5, cor="#555555")

    t.texto(650, 790, "C4 — Nível 2: diagrama de containers. Cada caixa é uma "
            "unidade implantável; os rótulos indicam o protocolo de comunicação.",
            tam=12.5, anc="middle", italico=True, cor="#555555")
    t.texto(650, 816, "O núcleo de domínio hexagonal vive dentro da API de "
            "Demandas; os demais containers o alcançam apenas por portas.",
            tam=12.5, anc="middle", italico=True, cor="#555555")
    return t.salvar("fig_c4_containers")


# =============================================================== figura 3
def hexagonal():
    t = Tela(1300, 820)
    cx, cy, r = 650, 400, 230

    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in (0, 60, 120, 180, 240, 300)]
    s = " ".join("%g,%g" % p for p in pts)
    t.add('<polygon points="%s" fill="#dff0e4" stroke="#1e6b3a" stroke-width="3"/>'
          % s)

    r2 = r - 56
    pts2 = [(cx + r2 * math.cos(math.radians(a)), cy + r2 * math.sin(math.radians(a)))
            for a in (0, 60, 120, 180, 240, 300)]
    s2 = " ".join("%g,%g" % p for p in pts2)
    t.add('<polygon points="%s" fill="#ffffff" stroke="#1e6b3a" stroke-width="2" '
          'stroke-dasharray="8 5"/>' % s2)

    t.texto(cx, cy - 92, "NÚCLEO DE DOMÍNIO", tam=15, peso="bold", anc="middle",
            cor="#1e6b3a")
    t.paragrafo(cx, cy - 62, [
        "Ocorrência · Categoria · Localização",
        "Prioridade · Situação · Bairro",
    ], tam=13, anc="middle", cor="#222222")
    t.texto(cx, cy + 2, "Regras de negócio", tam=13.5, peso="bold", anc="middle")
    t.paragrafo(cx, cy + 26, [
        "política de priorização por categoria,",
        "reincidência e impacto; máquina de",
        "situações da ocorrência; validação",
        "dos dados do registro",
    ], tam=12.5, anc="middle", cor="#333333")
    t.texto(cx, cy + 112, "não conhece HTTP, banco nem fornecedor", tam=12,
            anc="middle", italico=True, cor="#555555")

    t.texto(cx, cy - 168, "PORTAS", tam=13, peso="bold", anc="middle", cor="#1e6b3a")

    entradas = [
        (40, 150, "Adaptadores primários", None, None),
        (40, 196, "Controlador REST", "NestJS", "recebe POST /ocorrencias"),
        (40, 300, "Aplicativo móvel", "React Native", "mesmo contrato da API"),
        (40, 404, "Tarefa agendada", "cron", "reprioriza a fila diária"),
        (40, 508, "Console de administração", "React", "categorias e usuários"),
    ]
    for x, y, nome, tec, desc in entradas:
        if tec is None:
            t.texto(x, y, nome, tam=14, peso="bold", cor="#8a5a00")
            continue
        t.caixa(x, y, 270, 86, cor="ocre", r=8)
        t.texto(x + 135, y + 28, nome, tam=14, peso="bold", anc="middle")
        t.texto(x + 135, y + 48, "[%s]" % tec, tam=11.5, anc="middle", cor="#444444")
        t.texto(x + 135, y + 70, desc, tam=11.5, anc="middle", cor="#333333")
        t.seta(x + 274, y + 43, 420, cy - 60 + (y - 196) * 0.42)

    t.texto(40, 620, "porta de entrada: casos de uso", tam=12, italico=True,
            cor="#555555")
    t.paragrafo(40, 644, [
        "RegistrarOcorrencia · AtualizarSituacao",
        "PriorizarDemanda · ConsultarPainel",
    ], tam=12, cor="#555555")

    saidas = [
        (990, 150, "Adaptadores secundários", None, None),
        (990, 196, "Repositório PostgreSQL", "PostGIS", "persiste e consulta por área"),
        (990, 300, "Publicador de eventos", "RabbitMQ", "OcorrenciaRegistrada"),
        (990, 404, "Cliente de geocodificação", "API de mapas", "endereço → coordenada"),
        (990, 508, "Cliente do protocolo", "API da prefeitura", "abre protocolo oficial"),
    ]
    for x, y, nome, tec, desc in saidas:
        if tec is None:
            t.texto(x, y, nome, tam=14, peso="bold", cor="#1f4e79")
            continue
        t.caixa(x, y, 270, 86, cor="azul", r=8)
        t.texto(x + 135, y + 28, nome, tam=14, peso="bold", anc="middle")
        t.texto(x + 135, y + 48, "[%s]" % tec, tam=11.5, anc="middle", cor="#444444")
        t.texto(x + 135, y + 70, desc, tam=11.5, anc="middle", cor="#333333")
        t.seta(880, cy - 60 + (y - 196) * 0.42, x - 4, y + 43)

    t.texto(990, 620, "portas de saída: interfaces do domínio", tam=12,
            italico=True, cor="#555555")
    t.paragrafo(990, 644, [
        "OcorrenciaRepository · EventoPublisher",
        "GeocodificacaoGateway · ProtocoloGateway",
    ], tam=12, cor="#555555")

    t.texto(650, 740, "A dependência aponta sempre para dentro: o núcleo declara as "
            "portas, e os adaptadores as implementam.", tam=13, anc="middle",
            italico=True, cor="#555555")
    t.texto(650, 766, "Trocar o banco, o provedor de mapas ou o sistema da "
            "prefeitura é trocar um adaptador, sem tocar na regra de negócio.",
            tam=13, anc="middle", italico=True, cor="#555555")
    return t.salvar("fig_hexagonal")


# =============================================================== figura 4
def sequencia():
    t = Tela(1300, 1000)

    partic = [
        (110, ": Cidadão", "ator"),
        (320, ": Portal Web", "Interface"),
        (540, ": API de Demandas", "Adaptador REST"),
        (770, ": Serviço de Demandas", "Núcleo de domínio"),
        (990, ": Repositório", "PostgreSQL"),
        (1190, ": Publicador", "RabbitMQ"),
    ]
    topo, base = 70, 940
    for x, nome, papel in partic:
        larg = max(len(nome), len(papel)) * 8.0 + 24
        t.retangulo(x - larg / 2, topo, larg, 50, fundo="#ebebeb", borda="#3f3f3f",
                    traco=2)
        t.texto(x, topo + 22, nome, tam=13, peso="bold", anc="middle")
        t.texto(x, topo + 40, papel, tam=11, anc="middle", cor="#555555")
        t.linha(x, topo + 50, x, base, cor="#777777", larg=1.4, tracejado="7 6")

    def msg(n, x1, x2, y, texto, tam=12.5, retorno=False):
        cor = "#1f4e79" if not retorno else "#8a5a00"
        if retorno:
            t.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" '
                  'stroke-width="2" stroke-dasharray="7 5" marker-end="url(#pf)"/>'
                  % (x1, y, x2, y, cor))
        else:
            t.seta(x1, y, x2, y, cor=cor, larg=2.0)
        meio = (x1 + x2) / 2
        t.texto(meio, y - 9, "%s %s" % (n, texto), tam=tam, anc="middle")

    msg("1:", 110, 318, 168, "preenche e envia o formulário")
    t.texto(214, 186, "(categoria, descrição, localização, foto)", tam=11,
            anc="middle", cor="#555555")
    msg("2:", 320, 538, 214, "POST /ocorrencias")
    msg("3:", 540, 768, 252, "registrarOcorrencia(dados)")

    t.add('<rect x="763" y="272" width="14" height="40" fill="#ffffff" '
          'stroke="#555555" stroke-width="1.6"/>')
    t.seta(770, 282, 820, 282, cor="#1f4e79", larg=2.0)
    t.linha(820, 282, 820, 302, cor="#1f4e79", larg=2.0)
    t.add('<line x1="820" y1="302" x2="776" y2="302" stroke="#1f4e79" '
          'stroke-width="2" marker-end="url(#pf)"/>')
    t.texto(830, 278, "4: validar(dados)", tam=12.5)

    # ---- fragmento alt
    t.retangulo(60, 330, 1200, 570, fundo="none", borda="#9b1c31", traco=2.2, r=4)
    t.add('<polygon points="60,330 150,330 150,354 138,366 60,366" fill="#fadde2" '
          'stroke="#9b1c31" stroke-width="2.2"/>')
    t.texto(76, 352, "alt", tam=13.5, peso="bold", cor="#9b1c31")

    t.texto(170, 352, "[dados válidos e persistência disponível] — fluxo principal",
            tam=12.5, peso="bold", cor="#9b1c31")
    msg("5:", 770, 988, 400, "salvar(ocorrência, situação = ABERTA)")
    msg("6:", 990, 772, 436, "protocolo gerado", retorno=True)
    msg("7:", 770, 1188, 474, "publicar(OcorrenciaRegistrada)")
    msg("8:", 768, 542, 512, "protocolo", retorno=True)
    msg("9:", 538, 322, 548, "201 Created + protocolo", retorno=True)
    msg("10:", 320, 112, 584, "exibe o protocolo de acompanhamento", retorno=True)

    t.linha(60, 610, 1260, 610, cor="#9b1c31", larg=1.8, tracejado="9 6")
    t.texto(170, 634, "[dados inválidos] — fluxo alternativo A1", tam=12.5,
            peso="bold", cor="#9b1c31")
    msg("5a:", 768, 542, 672, "ErroDeValidacao(campos)", retorno=True)
    msg("6a:", 538, 322, 710, "422 com o erro por campo", retorno=True)
    msg("7a:", 320, 112, 746, "destaca os campos e solicita correção", retorno=True)

    t.linha(60, 772, 1260, 772, cor="#9b1c31", larg=1.8, tracejado="9 6")
    t.texto(170, 796, "[falha ao salvar] — fluxo alternativo A2", tam=12.5,
            peso="bold", cor="#9b1c31")
    msg("5b:", 988, 774, 834, "falha de persistência", retorno=True)
    msg("6b:", 538, 322, 870, "503 — indisponível, tente novamente", retorno=True)
    t.texto(690, 882, "7b: o Portal Web mantém o rascunho local e oferece reenvio; "
            "nenhum dado digitado pelo cidadão é perdido", tam=12, anc="middle",
            cor="#333333")

    t.texto(650, 964, "Cenário crítico: Registrar ocorrência. As mensagens "
            "tracejadas são retornos.", tam=12.5, anc="middle", italico=True,
            cor="#555555")
    return t.salvar("fig_sequencia")


# =============================================================== figura 5
def piramide():
    t = Tela(1260, 700)

    apice_y, base_y = 60, 540
    cx, meia = 330, 240

    def hw(y):
        return meia * (y - apice_y) / (base_y - apice_y)

    y1, y2 = 200, 360
    t.poligono([(cx - hw(y2), y2), (cx + hw(y2), y2),
                (cx + hw(base_y), base_y), (cx - hw(base_y), base_y)], cor="verde")
    t.poligono([(cx - hw(y1), y1), (cx + hw(y1), y1),
                (cx + hw(y2), y2), (cx - hw(y2), y2)], cor="azul")
    t.poligono([(cx, apice_y), (cx + hw(y1), y1), (cx - hw(y1), y1)], cor="ver")

    t.texto(cx, 172, "End-to-End", tam=18, peso="bold", anc="middle", cor="#9b1c31")
    t.texto(cx, 300, "Integração", tam=19, peso="bold", anc="middle", cor="#1f4e79")
    t.texto(cx, 460, "Unitários", tam=21, peso="bold", anc="middle", cor="#1e6b3a")
    t.texto(cx, 194, "poucos · caros · lentos", tam=11.5, anc="middle", cor="#9b1c31")
    t.texto(cx, 324, "alguns · custo médio", tam=12.5, anc="middle", cor="#1f4e79")
    t.texto(cx, 486, "muitos · rápidos · de baixo custo", tam=13, anc="middle",
            cor="#1e6b3a")

    t.caixa(650, 60, 580, 140, cor="ver")
    t.texto(670, 88, "End-to-End — o fluxo pelos olhos do usuário", tam=14.5,
            peso="bold", cor="#9b1c31")
    t.paragrafo(670, 114, [
        "E1  cidadão registra a ocorrência e recebe o protocolo",
        "E2  gestor prioriza, atualiza a situação e encerra",
        "E3  cidadão consulta o andamento pelo protocolo",
    ], tam=12.5)
    t.texto(670, 182, "execução noturna e antes de cada entrega", tam=11.5,
            italico=True, cor="#555555")

    t.caixa(650, 214, 580, 152, cor="azul")
    t.texto(670, 242, "Integração — a conversa entre as peças", tam=14.5,
            peso="bold", cor="#1f4e79")
    t.paragrafo(670, 268, [
        "API de ocorrências gravando e consultando no PostgreSQL",
        "consulta geoespacial por bairro com PostGIS",
        "publicação e consumo do evento OcorrenciaRegistrada",
        "adaptador de geocodificação e do protocolo da prefeitura",
        "upload de mídia no armazenamento de objetos",
    ], tam=12.5)

    t.caixa(650, 380, 580, 160, cor="verde")
    t.texto(670, 408, "Unitários — as regras, isoladas e sem E/S", tam=14.5,
            peso="bold", cor="#1e6b3a")
    t.paragrafo(670, 434, [
        "política de priorização por categoria, reincidência e impacto",
        "validação dos campos obrigatórios da ocorrência",
        "máquina de situações: Aberta → Em análise → Em execução →",
        "Concluída / Recusada, e as transições proibidas",
        "cálculo do prazo previsto por categoria",
    ], tam=12.5)

    t.caixa(60, 572, 1170, 104, cor="ocre", tracejado="8 5")
    t.texto(80, 600, "Critério de parada", tam=14, peso="bold", cor="#8a5a00")
    t.paragrafo(80, 626, [
        "Cobertura de 80 % de instruções e 70 % de ramos no pacote de domínio; "
        "sem meta para adaptadores gerados.",
        "Cobertura mede execução, não detecção: nenhuma funcionalidade é "
        "considerada pronta sem os critérios da Definition of Done.",
    ], tam=12.5)
    return t.salvar("fig_piramide")


if __name__ == "__main__":
    for f in (c4_contexto, c4_containers, hexagonal, sequencia, piramide):
        print(f())
