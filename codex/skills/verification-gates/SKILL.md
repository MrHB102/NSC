---
name: Verification Gates
description: Define provas mínimas antes de considerar uma tarefa concluída.
---

# Verification Gates

        ## Quando usar
        Toda tarefa não trivial.

        ## Porta de saída
        - testes executados
        - lint / typecheck relevantes
        - diff revisado
        - impacto descrito
        - rollback possível
        - nenhum arquivo inesperado alterado

        ## Regra
        Se não há verificação, não há conclusão.
