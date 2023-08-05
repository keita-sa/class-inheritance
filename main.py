import numpy as np

np.random.seed(123)


class Smoke(object):
    def __init__(self):
        self.con = 1.0
        self.x, self.y, self.z = 2.0, 0.0, 0.0
        self.vx, self.vy, self.vz = 0.05, 0.0, -0.1
        self.fx, self.fy, self.fz = 0.0, 0.0, 0.0

    def get_velocity(self):
        return self.vx, self.vy, self.vz

    def dynamics(self, dt):
        self.vx, self.vy, self.vz = self.get_velocity()
        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt
        new_z = self.z + self.vz * dt

    def eval_force(self):
        self.fx = np.random.randn()
        self.fy = np.random.randn()
        self.fz = np.random.randn()

    def update_velocity(self, dt):
        self.eval_force()
        self.vx += self.fx * dt
        self.vy += self.fy * dt
        self.vz += self.fz * dt


class HeavySmoke(Smoke):  # 継承するクラスを渡す
    def __init__(self):   # 継承したクラスでもinitが必要
        super().__init__()    # super()は親クラスを表す, 親クラスのinitを呼び出す
        self.mass = 1.0       # Smokeと違いHeavySmokeは質量を持ってる
        self.g_const = [0.0, 0.0, -9.8]  # 重力の影響を受ける、z軸方向に重力をかける


    def eval_force(self):     # override, 親クラスの上書き
        self.fx = np.random.randn() + self.mass * self.g_const[0]  # 重力が加わる
        self.fy = np.random.randn() + self.mass * self.g_const[1]
        self.fz = np.random.randn() + self.mass * self.g_const[2]

normal_smoke = Smoke()
heavy_smoke = HeavySmoke()

normal_smoke.eval_force()
print(normal_smoke.fz)

heavy_smoke.eval_force()
print(heavy_smoke.fz)