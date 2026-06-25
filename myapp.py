import streamlit as st

# 1. DATABASE YAKO NDOGO - Ongeza maneno hapa
financial_terms = {
    "Inflation": {
        "maana": "Kupanda kwa bei za bidhaa na huduma kwa ujumla kwa muda fulani. Pesa yako inakuwa na thamani ndogo.",
        "mfano": "Kilo 1 ya sukari ilikuwa TSH 2,500 mwezi uliopita, sasa ni TSH 3,000. Bei imepanda = Inflation.",
        "kiingereza": "Inflation"
    },
    "Dividend": {
        "maana": "Sehemu ya faida ya kampuni inayogawiwa kwa wenye hisa zake.",
        "mfano": "Ukinunua hisa za NMB, mwisho wa mwaka kampuni ikipata faida inakupa TSH 50 kwa kila hisa.",
        "kiingereza": "Dividend"
    },
    "Budget": {
        "maana": "Mpango wa matumizi ya pesa kwa kipindi fulani. Unapanga utatumia kiasi gani wapi.",
        "mfano": "Mshahara TSH 300,000: Kodi 50k, Chakula 100k, Akiba 50k. Hiyo ndio budget.",
        "kiingereza": "Budget"
    },
    "Loan": {
        "maana": "Pesa unayokopa kutoka benki au mtu mwingine na kuahidi kurudisha na riba.",
        "mfano": "Unakopa TSH 1,000,000 benki unarudisha TSH 1,200,000 baada ya mwaka 1.",
        "kiingereza": "Loan / Mkopo"
    },
    "Interest": {
        "maana": "Pesa ya ziada unayolipa au kupata kwa kukopa au kuweka pesa benki.",
        "mfano": "Ukiweka TSH 100,000 benki kwa riba 10%, mwaka utapata TSH 10,000 za ziada.",
        "kiingereza": "Interest / Riba"
    }, "Savings": {
        "maana": "Pesa unayoeka akiba badala ya kuitumia. Ni kwa ajili ya dharura au malengo ya baadaye.",
        "mfano": "Kila mwezi ukiweka TSH 20,000 benki, baada ya mwaka utakuwa na TSH 240,000 + riba.",
        "kiingereza": "Savings / Akiba"
    },
    "Investment": {
        "maana": "Kutumia pesa kununua kitu chenye uwezo wa kukupa faida zaidi baadaye.",
        "mfano": "Kununua hisa za Vodacom, kununua shamba, au kuanzisha biashara ndogo.",
        "kiingereza": "Investment / Uwekezaji"
    },
    "Profit": {
        "maana": "Faida. Pesa inayobaki baada ya kutoa gharama zote za biashara.",
        "mfano": "Ulinunua soda TSH 500, ukauza TSH 800. Profit yako ni TSH 300.",
        "kiingereza": "Profit / Faida"
    }, "Savings": {
        "maana": "Pesa unayoeka akiba badala ya kuitumia. Ni kwa ajili ya dharura au malengo ya baadaye.",
        "mfano": "Kila mwezi ukiweka TSH 20,000 benki, baada ya mwaka utakuwa na TSH 240,000 + riba.",
        "kiingereza": "Savings / Akiba"
    },
    "Investment": {
        "maana": "Kutumia pesa kununua kitu chenye uwezo wa kukupa faida zaidi baadaye.",
        "mfano": "Kununua hisa za Vodacom, kununua shamba, au kuanzisha biashara ndogo.",
        "kiingereza": "Investment / Uwekezaji"
    },
    "Profit": {
        "maana": "Faida. Pesa inayobaki baada ya kutoa gharama zote za biashara.",
        "mfano": "Ulinunua soda TSH 500, ukauza TSH 800. Profit yako ni TSH 300.",
        "kiingereza": "Profit / Faida"
    },
    "Loss": {
        "maana": "Hasara. Wakati gharama za biashara zinazidi pesa uliyopata.",
        "mfano": "Ulinunua mboga TSH 10,000 lakini ukauza TSH 8,000 tu. Umepata loss TSH 2,000.",
        "kiingereza": "Loss / Hasara"
    },
    "Tax": {
        "maana": "Pesa serikali inatoza kwa raia na biashara ili iendeshe huduma za umma.",
        "mfano": "VAT 18% unayolipa unaponunua simu, au PAYE inayokatwa mshaharani.",
        "kiingereza": "Tax / Kodi"
    },
    "VAT": {
        "maana": "Value Added Tax. Kodi ya 18% unayolipa kwa bidhaa na huduma nyingi Tanzania.",
        "mfano": "Simu ya TSH 100,000 + VAT 18% = utalipa TSH 118,000 dukani.",
        "kiingereza": "VAT"
    },
    "Insurance": {
        "maana": "Mkataba ambapo unalipa kiasi kidogo kila mwezi ili kampuni ikulipe ukipata hasara kubwa.",
        "mfano": "Bima ya gari: Ukiwa na ajali, kampuni ya bima inagharamia matengenezo.",
        "kiingereza": "Insurance / Bima"
    },
    "Credit Score": {
        "maana": "Alama inayoonyesha wewe ni mtu wa kuaminika kurudisha mkopo kwa wakati.",
        "mfano": "Ukikopa Tigo Pesa na kurudisha kwa wakati, credit score yako inapanda. Ni rahisi kukopa tena.",
        "kiingereza": "Credit Score"
    },
    "Compound Interest": {
        "maana": "Riba inayohesabiwa juu ya pesa yako + riba iliyopita. Inakua haraka.",
        "mfano": "TSH 100,000 kwa riba 10% compound: Mwaka 1 = 110k, Mwaka 2 = 121k, Mwaka 3 = 133k",
        "kiingereza": "Compound Interest"
    },
    "Asset": {
        "maana": "Kitu chochote chenye thamani na unachomiliki. Kinaweza kukupa pesa baadaye.",
        "mfano": "Nyumba, gari, simu, hisa, mashamba. Hizi zote ni assets.",
        "kiingereza": "Asset / Mali"
    },
    "Liability": {
        "maana": "Deni au wajibu wa kulipa pesa kwa mtu mwingine.",
        "mfano": "Mkopo wa benki, deni la kukodi nyumba, bill ya umeme. Hizi ni liabilities.",
        "kiingereza": "Liability / Deni"
    },
    "Cash Flow": {
        "maana": "Mwendo wa pesa kuingia na kutoka kwenye mfuko au biashara yako.",
        "mfano": "Mshahara unaingia TSH 300k, Kodi na chakula vinatoka TSH 250k. Cash flow yako +50k.",
        "kiingereza": "Cash Flow"
    },
    "Equity": {
        "maana": "Sehemu ya umiliki katika kampuni au mali baada ya kutoa madeni yote.",
        "mfano": "Nyumba ya TSH 100M, deni la benki TSH 40M. Equity yako ni TSH 60M.",
        "kiingereza": "Equity / Umiliki"
    },
    "Inflation Rate": {
        "maana": "Asilimia ya jinsi bei zinavyopanda kwa mwaka 1 mzima.",
        "mfano": "NBS ikisema inflation rate ni 4%, maana yake vitu kwa ujumla vimepanda 4% kuliko mwaka jana.",
        "kiingereza": "Inflation Rate"
    },
    "Withdrawal": {
        "maana": "Kutoa pesa kutoka benki, M-Pesa, au akiba yako.",
        "mfano": "Kuenda ATM kutoa TSH 50,000 au kutuma pesa kutoka M-Pesa kwenda benki.",
        "kiingereza": "Withdrawal / Utoaji"
    },
    "Deposit": {
        "maana": "Kuweka pesa benki, M-Pesa, au kwenye akiba yako.",
        "mfano": "Kuweka mshahara wako benki au kutuma pesa kutoka benki kwenda M-Pesa.",
        "kiingereza": "Deposit / Uwekaji"
    },
    "Balance": {
        "maana": "Kiasi cha pesa kilichobaki kwenye akaunti yako baada ya miamala yote.",
        "mfano": "Ukiangalia M-Pesa inaandika 'Balance: TSH 5,430'. Hiyo ndio iliyobaki.",
        "kiingereza": "Balance / Salio"
    },
    "Transaction": {
        "maana": "Kila kitendo cha kutuma, kupokea, au kubadilisha pesa.",
        "mfano": "Kutuma TSH 10,000 kwa rafiki, kulipia umeme, kununua bando. Zote ni transactions.",
        "kiingereza": "Transaction / Muamala"
    },
    "Risk": {
        "maana": "Uwezekano wa kupata hasara ukifanya uwekezaji au biashara fulani.",
        "mfano": "Kuwekeza crypto kuna risk kubwa - unaweza kupata faida kubwa au kupoteza yote.",
        "kiingereza": "Risk / Hatari"
    },
    "Revenue": {
        "maana": "Jumla ya pesa yote biashara imeipata kabla ya kutoa gharama.",
        "mfano": "Duka limeuza vitu TSH 2,000,000 mwezi huu. Hiyo yote ni revenue. Faida bado haijatoa gharama.",
        "kiingereza": "Revenue / Mapato"
    }

}

# 2. FUNCTION YA KUTAFUTA


def tafuta_neno(neno_iliyoandikwa):
    # inafanya "inflation" = "Inflation"
    neno_iliyoandikwa = neno_iliyoandikwa.strip().title()

    if neno_iliyoandikwa in financial_terms:
        data = financial_terms[neno_iliyoandikwa]
        st.success(f"✅ Neno: {neno_iliyoandikwa} / {data['kiingereza']}")
        st.write(f"*Maana:* {data['maana']}")
        st.info(f"*Mfano:* {data['mfano']}")
    else:
        st.error("❌ Samahani, neno halijapatikana bado kwenye database.")
        st.write("Jaribu maneno haya: " +
                 ", ".join(list(financial_terms.keys())))


# 3. DESIGN YA APP - STREAMLIT
st.set_page_config(page_title="Swahili Finance App", page_icon="📚")
st.title("📚 Swahili Financial Terms Explainer")
st.write("Jifunze maneno ya fedha kwa Kiswahili rahisi.")

neno = st.text_input("Andika neno la kifedha hapa:",
                     placeholder="mfano: Inflation, Budget...")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔍 Tafuta Maana", use_container_width=True):
        if neno:
            tafuta_neno(neno)
        else:
            st.warning("Tafadhali andika neno kwanza")

with col2:
    if st.button("📋 Onyesha Maneno Yote", use_container_width=True):
        st.write("*Maneno yaliyopo sasa hivi:*")
        st.write(", ".join(list(financial_terms.keys())))

st.divider()
st.caption("Project ya Field 2026")
