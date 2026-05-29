---
name: Multi-Service Boundaries
description: Protege contratos entre serviços e previne mudanças cross-service sem controle.
---

# Multi-Service Boundaries

        ## Quando usar
        Quando um change atravessa API, fila, worker, cache, banco ou frontend.

        ## Processo
        - identificar serviço origem
        - identificar serviço destino
        - documentar contrato
        - validar compatibilidade
        - escolher rollout seguro
        - prever fallback

        ## Regra
        Nunca misture refatoração interna com mudança de contrato no mesmo salto, sem justificativa forte.
