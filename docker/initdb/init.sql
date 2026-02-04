CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT
);

INSERT INTO users (name, email, age) VALUES
    ('山田太郎', 'yamada@example.com', 30),
    ('佐藤花子', 'sato@example.com', 25),
    ('鈴木一郎', 'suzuki@example.com', 35),
    ('テスト太郎', 'test-taro@example.com', 99);
