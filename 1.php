<?php
// 设置密码
$password = 'qwq0205.';

// 将密码与提交的密码进行比较
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $submittedPassword = $_POST['password'];
    if ($submittedPassword === $password) {
        // 密码正确，执行修改文件的逻辑
        
        // 声明初始变量
        $content = '';
        $message = '';
        
        // 检查是否提交了修改  
        if (isset($_POST['content'])) {
            // 获取新内容
            $newContent = $_POST['content'];

            // 校验新内容

            // 要修改的文件
            $file = '1.json';
            
            // 打开文件写入新内容
            $fp = fopen($file, 'w');
            if (fwrite($fp, $newContent)) {
                $message = '文件修改成功!';
            } else {
                $message = '文件修改失败!';
            }
            fclose($fp);

            // 重新读取文件内容
            $content = file_get_contents($file);
        } else {
            // 读取文件内容
            $file = '1.json';
            $content = file_get_contents($file);
        }

        // 显示当前内容
        echo '<pre>当前文件内容:' . htmlspecialchars($content) . '</pre>';

        // 显示成功或失败的消息
        if (!empty($message)) {
            echo '<pre>' . $message . '</pre>';
        }
    } else {
        // 密码错误，显示错误消息
        echo '<pre>密码错误，请重试!</pre>';
    }
}
?>

<form method="post">
    <input type="password" name="password" placeholder="请输入密码">
    <br>
    <textarea name="content" rows="10" cols="50"><?php echo htmlspecialchars($content); ?></textarea>
    <br>
    <button type="submit">修改</button> 
</form>