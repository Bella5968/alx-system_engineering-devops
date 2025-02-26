exec { 'fix-apache-error':
  command => 'apt-get update && apt-get install -y php libapache2-mod-php && systemctl restart apache2',
  onlyif  => 'test $(curl -s -o /dev/null -w "%{http_code}" 127.0.0.1) -eq 500',
}
