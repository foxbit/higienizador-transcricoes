# Higienizador de Transcrições

Aplicativo GTK4/Libadwaita para higienizar e melhorar transcrições, integrando a API Gemini do Google.

## Recursos
- Limpeza de textos (remoção de hesitações e correções)
- Resumo e formatação
- Suporte a formatos TXT, SRT, VTT e exportação para DOCX
- Interface moderna com Libadwaita
- Configurações persistentes via GSettings
- Armazenamento seguro de API Key com SecretStorage
- Build com Meson e distribuição via Flatpak

## Instalação
Consulte `INSTALACAO.md` para instruções detalhadas de instalação.

## Uso
1. Abra um arquivo de transcrição ou cole texto
2. Configure a API Key do Gemini nas preferências
3. Escolha o tipo de processamento e execute
4. Exporte o resultado no formato desejado

## Desenvolvimento
- `build.py` controla setup, build, testes e Flatpak
- `meson.build` e `meson_options.txt` definem o projeto Meson
- `com.foxbit.higienizador.yml` é o manifesto Flatpak

## Licença
GPL-3.0. Veja `LICENSE`.
