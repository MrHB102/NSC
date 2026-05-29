---
name: Legacy Safe Change
description: Evita quebrar comportamento implícito em código legado.
---

# Legacy Safe Change

        ## Quando usar
        Em qualquer mudança dentro de um monorepo, sistema antigo, ou módulo com muita história.

        ## Processo
        1. Descubra comportamento atual.
        2. Identifique contratos públicos.
        3. Separe refatoração de alteração funcional.
        4. Prefira mudanças pequenas e reversíveis.
        5. Preserve compatibilidade até ter prova do contrário.

        ## Anti-padrão
        Não "limpar" legado sem medir o impacto.
