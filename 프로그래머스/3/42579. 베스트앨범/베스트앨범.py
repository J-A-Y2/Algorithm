# 장르의 인덱스와 재생 횟수 인덱스를 일치 시킨다.
# 가장 많이 재생된 순으로 정렬한다.
# 
def solution(genres, plays):
    # 장르별로 노래의 재생 횟수를 저장할 딕셔너리
    genre_play_count = {}
    # 장르별로 노래의 정보를 저장할 딕셔너리
    genre_songs = {}
    
    # 장르별로 노래의 재생 횟수 합산
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
            genre_songs[genre] = []
        genre_play_count[genre] += play_count
        genre_songs[genre].append((i, play_count))
    
    # 장르별로 노래의 재생 횟수로 내림차순 정렬
    sorted_genre = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    # 장르별로 노래 선택
    for genre, _ in sorted_genre:
        # 재생 횟수로 내림차순 정렬
        genre_songs[genre].sort(key=lambda x: (-x[1], x[0]))
        # 최대 두 개의 노래 선택
        selected_songs = genre_songs[genre][:2]
        for song in selected_songs:
            answer.append(song[0])
    
    return answer