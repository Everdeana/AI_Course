/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode : false,
    swcMinify: true,
    async rewrites() {
        return [
            {
                source: "/v1/:path*",
                destination: "http://localhost:8000/api/v1/:path*",
            },
        ];
    },
};

export default nextConfig;
