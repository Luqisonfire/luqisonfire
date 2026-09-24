# Lucas de Sousa Corrêa

Desenvolvedor Backend Júnior · JavaScript/TypeScript (Node.js) · Python

Santo André – SP · Remoto · [SEU TELEFONE] · [SEU E-MAIL] · [linkedin.com/in/luqisonfire](https://www.linkedin.com/in/luqisonfire) · [github.com/luqisonfire](https://github.com/luqisonfire)

## Resumo

Desenvolvedor com sistemas próprios em produção no financeiro de uma empresa de viagens corporativas: integrações entre sistemas, automação de processos fiscais e aplicações web com arquitetura em camadas. Atuo junto à área de negócio, do levantamento de requisitos à manutenção. Programo em JavaScript/TypeScript (Node.js) e Python, com PostgreSQL e SQLite, e trato testes automatizados e Git como parte da entrega. Busco minha primeira posição formal como Desenvolvedor Backend, com interesse no mercado financeiro e em Open Finance.

## Competências técnicas

- **Linguagens:** JavaScript, TypeScript, Python, SQL
- **Backend:** Node.js, APIs REST, Flask, Next.js (Server Actions), Prisma, validação com Zod, autenticação e controle de acesso por perfil
- **Bancos de dados:** PostgreSQL, SQLite, migrações
- **Integração e automação:** extensões Chrome (Manifest V3), Native Messaging, OCR (Tesseract), Playwright, pandas
- **Qualidade:** testes automatizados (Vitest, pytest, Playwright), ESLint, Biome, ruff, mypy, ADRs, Git/GitHub (branches e pull requests)
- **Frontend e design (complementar):** React, Dash, HTML/CSS, identidade visual e design system

## Experiência

Assistente Financeiro — responsável técnico por soluções internas04/2025 – atual

Compra Direta Gestão de Viagens Corporativas · São Paulo

Criei a frente de desenvolvimento interno do financeiro, que não existia: levanto a demanda com o time, estimo, desenvolvo, coloco em produção e mantenho.

- **ROG Kandir — reembolso Lei Kandir no portal ROG da LATAM:** extensão Chrome (MV3) em JavaScript com native host em Node.js e OCR em Python (PyMuPDF + Tesseract). Lê e padroniza as DARFs por OCR, validando os valores por aritmética; concilia STUR × LATAM × DARFs e aponta divergências de base; preenche a solicitação no portal e acompanha o status pela API REST do portal; controla solicitações e bilhetes já incluídos, renomeia pastas por status e monta o e-mail. Regra fiscal isolada em camada de domínio, 35 suítes de testes e decisões registradas em ADRs.
- **Tower — integração de vendas e rotinas operacionais (Argo/Travel Agent → Sturweb):** extensão Chrome (MV3) em JavaScript que captura a reserva e lança a venda no ERP aplicando as regras da agência e de cada cliente (produto, emissor, fee, centro de custo, recebimentos e pagamentos). Valida os dados antes das etapas financeiras e interrompe quando algo não confere. Inclui rotinas de reembolso e correção de cartão; 59 suítes de testes em Node.js.
- **Dashboard financeiro (Python, Flask + Dash):** refatorei um app de arquivo único (~1.800 linhas) para arquitetura em camadas; autenticação com bcrypt e perfis de acesso; endpoint REST idempotente (`POST /api/sync/emails`) com limite de payload para sincronizar dados do Outlook; suporte a SQLite e PostgreSQL com script de migração. 162 testes (pytest, unidade e integração), ruff e mypy.
- **Conciliação LATAM × Stur Web:** rotina que cruza os dados dos dois sistemas pelo número do bilhete, substituindo a conferência manual linha a linha.

Experiências anteriores

- **Atendente** — St. Marche · 02/2025 – 04/2025  ·  **Banhista e Tosador** — Petshop Skina dos Bichos e Petshop Amicão · 2017 – 2025

## Projeto voluntário

Protetores do ABC — site e painel de gestão para ONG de proteção animalem construção

- Projeto voluntário feito de ponta a ponta por mim, da identidade visual e do design system ao backend. Aplicação em Next.js, React e TypeScript com PostgreSQL via Prisma. Escrita por Server Actions com validação em Zod e autorização por sessão e papel; login da equipe por Google com lista de acesso; dados enviados pelo público ficam em fila de triagem antes de entrar na base. 201 testes em Vitest, testes ponta a ponta com Playwright e documentação de requisitos, arquitetura e segurança.

## Formação e idiomas

**Tecnólogo em Análise e Desenvolvimento de Sistemas** — Uninove06/2023 – 12/2025

**Idiomas:** Português (nativo) · Inglês (intermediário, leitura de documentação técnica)
