import streamlit as st

class AzureRecommendationSystem:
    def __init__(self, vm_security, vm_backup, vm_disaster_recovery):
        self.vm_security = vm_security
        self.vm_backup = vm_backup
        self.vm_disaster_recovery = vm_disaster_recovery

    def evaluate_security(self):
        if self.vm_security == 'Ninguna':
            return "ALTO - Implementa Microsoft Defender for Cloud, Just-In-Time VM Access y Azure Firewall."
        elif self.vm_security == 'Básica':
            return "MEDIO - Agrega Azure Key Vault y Network Security Groups más estrictos."
        else:
            return "BAJO - Seguridad en buen estado, revisa logs con Azure Monitor."
    
    def evaluate_backup(self):
        if self.vm_backup == 'No Configurado':
            return "ALTO - Habilita Azure Backup para protección ante fallos y ataques."
        else:
            return "BAJO - Backup configurado correctamente, revisa políticas de retención."
    
    def evaluate_disaster_recovery(self):
        if self.vm_disaster_recovery == 'No Configurado':
            return "ALTO - Implementa Azure Site Recovery para failover en otra región."
        else:
            return "BAJO - DRP configurado correctamente, revisa pruebas de failover periódicas."
    
    def generate_recommendations(self):
        return {
            "Seguridad": self.evaluate_security(),
            "Backup": self.evaluate_backup(),
            "Recuperación ante Desastres": self.evaluate_disaster_recovery()
        }

# Interfaz con Streamlit
st.title("Sistema de Recomendaciones para Azure")

vm_security = st.selectbox("Nivel de Seguridad en las VMs", ["Ninguna", "Básica", "Avanzada"])
vm_backup = st.selectbox("Configuración de Backup", ["No Configurado", "Configurado"])
vm_disaster_recovery = st.selectbox("Recuperación ante Desastres", ["No Configurado", "Configurado"])

if st.button("Generar Recomendaciones"):
    cliente = AzureRecommendationSystem(vm_security, vm_backup, vm_disaster_recovery)
    recomendaciones = cliente.generate_recommendations()
    
    for area, recomendacion in recomendaciones.items():
        st.write(f"**{area}:** {recomendacion}")
