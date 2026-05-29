# Fragile Zones

Onde um agente tende a quebrar o sistema:

- acoplamento entre serviços
- lógica de autenticação
- billing
- sincronização de dados
- migrações de schema
- workers e jobs idempotentes
- feature flags
- código com efeitos colaterais implícitos

Para cada zona:
- arquivos principais
- testes existentes
- rollback
- blast radius
