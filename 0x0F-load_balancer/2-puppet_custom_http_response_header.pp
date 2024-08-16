# Install and configure HAproxy 

exec {'update':
  command  => 'sudo apt-get -y update',
}

package {'Nginx':
  ensure => 'installed',
  require   => Exec['update'],
}

file {'/var/www/html/index.html':
  content => 'Hello world'
}

exec{'redirect_me':
  command => 'sed -i "24i\    rewrite ^\redirect_me https://www.google.com/;" /etc/nginx/sites_available/default',
  provider => 'shell', 

}

exec { 'HTTP header':
  command => 'sed -i 25i\    add_header" X-Served-By \$hostname;" /etc/nginx/sites_available/default',
  provider => 'shell',
}

service {'nginx':
  ensure => 'running',
  require => package['Nginx],
}

