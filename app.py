import streamlit as st

def calculate_score(answers):
    categories = {
        "Stres Akademik": [0, 3, 11],
        "Depresi": [1, 5, 12, 18],
        "Kecemasan": [4, 7, 16, 17],
        "Bullying": [2, 8],
        "Gangguan Makan": [6, 9],
        "Masalah Identitas": [10, 15],
        "Ketergantungan Teknologi": [13, 14, 19]
    }
    
    scores = {category: sum(answers[q] for q in indices) for category, indices in categories.items()}
    return scores

def main():
    st.title("Kalkulator Kesehatan Mental")

    st.write("Jawablah pertanyaan berikut dengan skala 0-4 (0: Tidak pernah, 4: Selalu)")

    questions = [
        "Saya merasa tertekan dengan tugas akademik",
        "Saya merasa sedih atau depresi",
        "Saya merasa diintimidasi oleh orang lain",
        "Saya sulit berkonsentrasi pada pelajaran",
        "Saya merasa cemas tanpa alasan yang jelas",
        "Saya kehilangan minat pada aktivitas yang biasanya saya nikmati",
        "Saya khawatir tentang berat badan atau penampilan saya",
        "Saya merasa gugup atau cemas dalam situasi sosial",
        "Saya merasa tidak aman di sekolah/kampus",
        "Saya membatasi makanan saya secara ketat",
        "Saya merasa bingung tentang identitas diri saya",
        "Saya merasa kewalahan dengan beban akademik",
        "Saya merasa putus asa tentang masa depan",
        "Saya menghabiskan terlalu banyak waktu online",
        "Saya merasa cemas jika tidak bisa mengakses ponsel atau internet",
        "Saya merasa sulit untuk mengekspresikan diri saya",
        "Saya merasa tegang atau gelisah",
        "Saya merasa sulit untuk rileks",
        "Saya memiliki pikiran untuk menyakiti diri sendiri",
        "Saya merasa teknologi mengganggu hubungan sosial saya"
    ]

    answers = []
    for i, question in enumerate(questions):
        answer = st.slider(f"Q{i+1}: {question}", 0, 4, 0)
        answers.append(answer)

    if st.button("Hitung Skor"):
        scores = calculate_score(answers)
        max_category = max(scores, key=scores.get)
        
        st.write("Hasil:")
        for category, score in scores.items():
            st.write(f"{category}: {score}")
        
        st.write(f"\nBerdasarkan jawaban Anda, kategori dengan skor tertinggi adalah: **{max_category}**")
        
        if max_category == "Stres Akademik":
            st.write("Anda mungkin mengalami stres akademik. Cobalah untuk mengatur waktu dengan lebih baik dan jangan ragu untuk meminta bantuan jika diperlukan.")
        elif max_category == "Depresi":
            st.write("Anda mungkin mengalami gejala depresi. Disarankan untuk berkonsultasi dengan profesional kesehatan mental.")
        elif max_category == "Kecemasan":
            st.write("Anda mungkin mengalami kecemasan. Teknik relaksasi dan mindfulness mungkin bisa membantu.")
        elif max_category == "Bullying":
            st.write("Anda mungkin terdampak bullying. Penting untuk berbicara dengan seseorang yang Anda percaya atau pihak berwenang di sekolah/kampus.")
        elif max_category == "Gangguan Makan":
            st.write("Anda mungkin mengalami masalah terkait pola makan. Konsultasikan dengan ahli gizi atau psikolog untuk mendapatkan bantuan.")
        elif max_category == "Masalah Identitas":
            st.write("Anda mungkin mengalami masalah terkait identitas diri. Berbicara dengan konselor atau psikolog bisa membantu Anda memahami diri lebih baik.")
        elif max_category == "Ketergantungan Teknologi":
            st.write("Anda mungkin mengalami ketergantungan teknologi. Cobalah untuk membatasi penggunaan teknologi dan temukan kegiatan offline yang menyenangkan.")

        st.write("\nPeringatan: Hasil ini hanya indikasi awal dan bukan diagnosis medis. Jika Anda memiliki kekhawatiran serius tentang kesehatan mental Anda, silakan konsultasikan dengan profesional kesehatan mental.")

if __name__ == "__main__":
    main()

    #2,4,3,1,1,0,4,4,0,0,1,1,0,4,4,4,2,0,0,0