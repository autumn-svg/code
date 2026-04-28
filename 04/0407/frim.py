2 6 25
3 4 34
3 5 18
4 5 48
4 * 6 51
#힙에 가중치를 기준으로 원소를 삽입, 제거 
# 원소를 제거 -> 가중치가 가장 작은 원소가 뜸
from heapq import haeapppp, heappush

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())

G = p[ for _ in range(V)]

for i in range(E)
    s,e, w = map(int, input().split())
    G[s].append((e, w))
    G[e].append((s, w))
    
    '''
    1. 임의의 정점을 하나 골라서 지각
    2. 내가 지금까지 골랐던 정점들과 인접하는 정접 중에 최소 가둥치를 가진 간선을 선택(조건: 이전에 선택한 적 없는 정점과 이어진 간선)
    
    3. MST가 만들어질때까지 반복
    '''
    
    #start: 시작 쟁점 번호
    
def prim(start):
    
    #우선순위큐(최소힙)
    heap = [(가중치, 정점번호)]
    #중복체크 배열
    # MsT[i] = 1: i번 정점은 MST에 포함
    # MST [i] = 0:i번 정점은 미포함
    
    MST = [0] * V
    
    #최소 비용
    min_w = 0
  
    
# 힙에 시작정점 추가
# (가중치, 정점 번호) 형태로 힙에 추가, 
# 이때 힙의 운선순위 선정 기준은 튜플의 원소
#   시작정점을 추가할 때는  가중치를 0으로
heapppush(heap,(0),start))
